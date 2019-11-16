<div id="container"></div>
<script async
  src="https://pay.google.com/gp/p/js/pay.js"
  onload="onGooglePayLoaded()"> 
</script>

<script>
    const baseRequest = {
      apiVersion: 2,
      apiVersionMinor: 0
    };

    const allowedCardNetworks = ["AMEX", "DISCOVER", "INTERAC", "JCB", "MASTERCARD", "VISA"];
    const allowedCardAuthMethods = ["PAN_ONLY", "CRYPTOGRAM_3DS"];

    const tokenizationSpecification = {x
        "type": "DIRECT",
        "parameters": {
        "protocolVersion": "ECv2",
        "key=API_KEY": "AIzaSyCRq4xiasSjvfLYwj7B_o-MWZqHL3082gY"
        }
        /** ou por gatway 
                const tokenizationSpecification = {
                    type: 'PAYMENT_GATEWAY',
                    parameters: {
                        'gateway': 'example',
                        'gatewayMerchantId': 'exampleGatewayMerchantId'
                    }
                };
        */
    }


    const baseCardPaymentMethod = {
      type: 'CARD',
      parameters: {
        allowedAuthMethods: allowedCardAuthMethods,
        allowedCardNetworks: allowedCardNetworks
      }
    };

    const cardPaymentMethod = Object.assign(
      {},
      baseCardPaymentMethod,
      {
        tokenizationSpecification: tokenizationSpecification
      }
    );

    function getGoogleIsReadyToPayRequest() {
      return Object.assign(
          {},
          baseRequest,
          {
            allowedPaymentMethods: [baseCardPaymentMethod]
          }
      );
    }

    function getGooglePaymentDataRequest() {
      const paymentDataRequest = Object.assign({}, baseRequest);
      paymentDataRequest.allowedPaymentMethods = [cardPaymentMethod];
      paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
      paymentDataRequest.merchantInfo = {
        // @todo a merchant ID is available for a production environment after approval by Google
        // See {@link https://developers.google.com/pay/api/web/guides/test-and-deploy/integration-checklist|Integration checklist}
        // merchantId: '01234567890123456789',
        merchantName: 'Example Merchant'
      };

      paymentDataRequest.callbackIntents = ["PAYMENT_AUTHORIZATION"];

      return paymentDataRequest;
    }

    function getGooglePaymentsClient() {
      if ( paymentsClient === null ) {
        paymentsClient = new google.payments.api.PaymentsClient({
            environment: 'TEST',
          paymentDataCallbacks: {
            onPaymentAuthorized: onPaymentAuthorized
          }
        });
      }
      return paymentsClient;
    }

    function onPaymentAuthorized(paymentData) {
            return new Promise(function(resolve, reject){
        // handle the response
        processPayment(paymentData)
        .then(function() {
          resolve({transactionState: 'SUCCESS'});
        })
        .catch(function() {
          resolve({
            transactionState: 'ERROR',
            error: {
              intent: 'PAYMENT_AUTHORIZATION',
              message: 'Insufficient funds',
              reason: 'PAYMENT_DATA_INVALID'
            }
          });
            });
      });
    }

    function onGooglePayLoaded() {
      const paymentsClient = getGooglePaymentsClient();
      paymentsClient.isReadyToPay(getGoogleIsReadyToPayRequest())
          .then(function(response) {
            if (response.result) {
              addGooglePayButton();
            }
          })
          .catch(function(err) {
            // show error in developer console for debugging
            console.error(err);
          });
    }

    function addGooglePayButton() {
      const paymentsClient = getGooglePaymentsClient();
      const button =
          paymentsClient.createButton({onClick: onGooglePaymentButtonClicked});
      document.getElementById('container').appendChild(button);
    }

    function getGoogleTransactionInfo() {
      return {
            displayItems: [
            {
              label: "Subtotal",
              type: "SUBTOTAL",
              price: "11.00",
            },
          {
              label: "Tax",
              type: "TAX",
              price: "1.00",
            }
        /** adicionar taxas e direcionar para o shopdin
         * 12% total 
         * 2% ong
         * 4% cashback
         * 6% shopdin
         */
        ],
        currencyCode: "BRL",
        totalPriceStatus: "FINAL",
        totalPrice: "12.00",
        totalPriceLabel: "Total"
      };
    }

    function onGooglePaymentButtonClicked() {
      const paymentDataRequest = getGooglePaymentDataRequest();
      paymentDataRequest.transactionInfo = getGoogleTransactionInfo();

      const paymentsClient = getGooglePaymentsClient();
      paymentsClient.loadPaymentData(paymentDataRequest);
    }

    function processPayment(paymentData) {
            return new Promise(function(resolve, reject) {
            setTimeout(function() {
                    // @todo pass payment token to your gateway to process payment
                    paymentToken = paymentData.paymentMethodData.tokenizationData.token;

            resolve({});
        }, 3000);
      });
    }
</script>