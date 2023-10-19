-- </Definições Globais


larguraTela = love.graphics.getWidth() 
alturaTela = love.graphics.getHeight()
speedBuster = 10


animacao = require("anim8")

-- Definições Globais />

function love.load()  
    -- </Geral
    continuaJogando = true
    pontuacao = 0
    health = 2
    -- Geral />

    upgradeOptions = {
        "movespeed",
        "bulletspeed",
        "bulletdelay"
    }
    local spawnedUpgrade = nil

    -- </ Efeitos sonoros
    fireSound = love.audio.newSource("sons/tiro.wav", "static")
    shipExplosionSound = love.audio.newSource("sons/ExplodeNave.wav", "static")
    enemyExplosionSound = love.audio.newSource("sons/ExplodeInimigo.wav", "static")
    musicBackground = love.audio.newSource("sons/Musica.wav", "static")
    musicBackground:play()
    musicBackground:setLooping(true)
    -- Efeitos sonoros />

    -- </ Background
    fundoA = love.graphics.newImage("imagens/Background.png")
    fundoB = love.graphics.newImage("imagens/Background.png")
    planoFundo =
    {
        x = 0,
        yA = 0,
        yB = 0 - fundoA:getHeight(),
        speed = 5 * speedBuster
    }
    -- Background/>

    -- </ Nave
    imgNave = love.graphics.newImage("imagens/Nave.png")
    imgNaveB = love.graphics.newImage("imagens/NaveB.png")
    nave =
    {
        x = (larguraTela / 2) - (imgNave:getWidth() / 2),
        y = alturaTela / 2,
        speed = 20 * speedBuster
    }
    -- Nave/>

    -- </Inimigos
    enemyDelay = 1
    enemyTimeout = enemyDelay
    enemyTable = {}
    enemyspeed = nave.speed / 20
    -- Inimigos/>

    -- </Caça Inimigo
    enemyFighter = love.graphics.newImage("imagens/inimigo.png")
    -- Caça Inimigo/>

    -- </Ataque
    hitFire = true
    fireSpeed = 50
    fireDelay = 0.8
    fireTimeout = fireDelay
    fireTable = {}
    -- Ataque/>

    -- </Projétil
    imgProjetil = love.graphics.newImage("imagens/Projetil.png")    
    -- Projétil/>

    -- </Fonte
    imgFonte = love.graphics.newImageFont("imagens/Fonte.png", " abcdefghijklmnopqrstuvwxyz" .. "ABCDEFGHIJKLMNOPQRSTUVWXYZ0" .. "123456789.,!?-+/():;%&`'*#=[]\"")
    -- Fonte/>

    -- </Efeito
    escalaX = 1
    escalaY = 1
    efeitoX = 3.5
    efeitoY = 3.5
    -- Efeitos/>

    -- </Explode Inimigo
    spriteExpInimigo = love.graphics.newImage("imagens/Explosao.png")
    expInimigo = { }
    expInimigo.x = 0
    expInimigo.y = 0
    local gridExplosao = animacao.newGrid(64, 64, spriteExpInimigo:getWidth(), spriteExpInimigo:getHeight())
    ExplodeInimigo = animacao.newAnimation(gridExplosao('1-5', 1, '1-5', 2, '1-5', 3, '1-5', 4, '1-5', 5, '1-5', 6), 0.01, executaAnimacao)
    -- Explode Inimigo/>
end

function love.update(dt)
    -- </ Background
    MovimentacaoPlanoFundo(dt)
    -- Background/>

    -- </ Efeito do Placar
    efeitoPlacar(dt)
    -- Efeito do Placar/>

    -- </ Nave
    movimentacaoNave(dt)
    -- Nave/>

    -- </ Atacar (tocar o terror)
    atacar(dt)
    -- Atacar/>

    -- </ Inimigo
    ataqueInimigo(dt)
    -- Inimigo/>

    -- </ Controle das explosoes
    controlaExplosao(dt)
    -- Controle das explosoes/>
    
    -- </ Detectar Colisões
    detectarColisoes()
    -- Detectar Colisões/>

    handleUpgrade()
    

    -- </ Verificar se o jogador digitou r para reiniciar o jogo
    if not continuaJogando and love.keyboard.isDown("r") then
        fireTable = {}
        enemyTable = {}
        hitFire = true
        fireTimeout = fireDelay
        enemyTimeout = enemyDelay
        nave.x = larguraTela / 2
        nave.y = alturaTela / 2
        pontuacao = 0
        continuaJogando = true
    end
    -- Verificar se o jogador digitou r para reiniciar o jogo/>    
end

function love.draw()
    -- </ Background
    love.graphics.draw(fundoA, planoFundo.x, planoFundo.yA);
    love.graphics.draw(fundoB, planoFundo.x, planoFundo.yB);
    -- Background/>

    -- </ Pontos na tela
    love.graphics.setFont(imgFonte)
    love.graphics.print("Placar: ", 10, 10, 0, 1, 1, 0, 2, 0, 0)
    love.graphics.print(pontuacao, 90, 14, 0, escalaX, escalaY, 5, 5, 0, 0)
    -- Pontos na tela />

    -- </ Game over e reiniciar
    if not continuaJogando then
        love.graphics.print("Aperte 'r' para reiniciar.", larguraTela/3, alturaTela/2)
    end
    -- Game over e reiniciar />

    -- </ Nave
    if continuaJogando then
        love.graphics.draw(imgNave, nave.x, nave.y);
        if health == 1 then
            love.graphics.draw(imgNaveB, nave.x, nave.y);
        end
    end
    -- Nave/>

    -- </Ataque Inimigo
    for i, item in ipairs(enemyTable) do
        love.graphics.draw(item.img, item.x, item.y)
    end
    -- Ataque Inimigo/>

    -- </Explode Inimigo
    for i, _ in ipairs(expInimigo) do
        ExplodeInimigo:draw(spriteExpInimigo, expInimigo.x, expInimigo.y)
    end
    -- Explode Inimigo/>

    -- </Ataques
    for i, item in ipairs(fireTable) do
        love.graphics.draw(item.img, item.x, item.y)
    end
    -- Ataques/>

    if spawnedUpgrade ~= nil then
        love.graphics.printf(spawnedUpgrade, 0, 0, love.graphics.getWidth(), "center")
    end
    
end

function controlaExplosao(dt)
    for i, _ in ipairs(expInimigo) do
        ExplodeInimigo:update(dt)
    end
end

function executaAnimacao()
    for i, _ in ipairs(expInimigo) do
        table.remove(expInimigo, i)
    end
end

function efeitoPlacar(dt)
    escalaX = escalaX - 3 * dt
    escalaY = escalaY - 3 * dt

    if (escalaX <= 1) then
        escalaX = 1
        escalaY = 1
    end
end

function colidiu( x1, y1, h1, w1, x2, y2, h2, w2 )
    return x1 < (x2 + w2) and x2 < (x1 + w1) and y1 < (y2 + h2) and y2 < (y1 + h1)
end

function detectarColisoes()
    for i, enemy in ipairs(enemyTable) do
        for j, fire in pairs(fireTable) do
            if colidiu(enemy.x, enemy.y, enemyFighter:getHeight(), enemyFighter:getWidth(), fire.x, fire.y, imgProjetil:getHeight(), imgProjetil:getWidth()) then
                table.remove(fireTable, j)
                table.remove(enemyTable, i)
                expInimigo.x = enemy.x
                expInimigo.y = enemy.y
                table.insert(expInimigo, ExplodeInimigo)
                enemyExplosionSound:stop()
                enemyExplosionSound:play()
                escalaX = efeitoX
                escalaY = efeitoY
                
                pontuacao = pontuacao + 1
                if pontuacao % 5 == 0 then
                    health = health + 1
                elseif health >= 2 then
                    health = 2
                end
            end        
        end
        if colidiu(enemy.x, enemy.y, enemyFighter:getHeight(), enemyFighter:getWidth(), nave.x - (imgNave:getWidth()/2), nave.y, imgNave:getHeight(), imgNave:getWidth()) and continuaJogando then
            table.remove(enemyTable, i)
            shipExplosionSound:stop()
            shipExplosionSound:play()
            
            health = health - 1
            if health <= 0 then
                continuaJogando = false
            end
        end
    end
end

function atacar(dt)
    fireTimeout = fireTimeout - (1 * dt)

    if fireTimeout < 0 then
        hitFire = true
    end

    if continuaJogando then
        if love.keyboard.isDown("space") and hitFire then
            newFire = { x = nave.x + ((imgNave:getWidth() / 2) - 5), y = nave.y, img = imgProjetil }
            table.insert(fireTable, newFire)
            hitFire = false
            fireTimeout = fireDelay
            fireSound:stop()
            fireSound:play()
        end
    end

    for i, item in ipairs(fireTable) do
        item.y = item.y - ((fireSpeed * speedBuster) * dt)
        if item.y < -imgProjetil:getHeight()  then
            table.remove(fireTable, i)
        end
    end      
end

function ataqueInimigo(dt)
    enemyTimeout = enemyTimeout - (1 * dt)

    if enemyTimeout < 0 then
        enemyTimeout = enemyDelay
        novaPosicao = math.random(10, love.graphics.getWidth() - ((enemyFighter:getWidth() / 2) + 10))
        newEnemy = { x = novaPosicao, y = -enemyFighter:getHeight(), img = enemyFighter }
        table.insert(enemyTable, newEnemy)
    end

    for i, item in ipairs(enemyTable) do
        item.y = item.y + ((enemyspeed * speedBuster) * dt)
        if item.y > alturaTela then
        table.remove(enemyTable, i)
        end
    end
end

function MovimentacaoPlanoFundo(dt)
    planoFundo.yA = planoFundo.yA + planoFundo.speed * dt
    planoFundo.yB = planoFundo.yB + planoFundo.speed * dt

    if (planoFundo.yA > alturaTela) then
        planoFundo.yA = planoFundo.yB - fundoA:getHeight()
    end

    if (planoFundo.yB > alturaTela) then
        planoFundo.yB = planoFundo.yA - fundoB:getHeight()
    end
end

function movimentacaoNave(dt)
    -- Mover para cima (up)
    if (love.keyboard.isDown("up")) then
        if (nave.y > 0) then
            nave.y = nave.y - (nave.speed * dt)
        end
    end

    -- Mover para baixo (down)
    if (love.keyboard.isDown("down")) then
        if (nave.y < alturaTela - imgNave:getHeight()) then
            nave.y = nave.y + (nave.speed * dt)
        end
    end

    -- Mover para esquerda (left)
    if (love.keyboard.isDown("left")) then
        if (nave.x > 0) then
            nave.x = nave.x - (nave.speed * dt)
        end
    end

    -- Mover para esquerda (right)
    if (love.keyboard.isDown("right")) then
        if (nave.x < larguraTela - imgNave:getWidth()) then
            nave.x = nave.x + (nave.speed * dt)
        end
    end
end

function handleUpgrade()
    if pontuacao % 3 == 0 and spawnedUpgrade == nil then
        local randomIndex = love.math.random(1, #upgradeOptions)
        spawnedUpgrade = upgradeOptions[randomIndex]
    
        if bulletspeed then
            fireSpeed = fireSpeed + 100
        end
        if bulletdelay then
            fireDelay = fireDelay - 0.8
        end
        if movespeed then
            nave.speed = nave.speed + 100
        end
    end
end