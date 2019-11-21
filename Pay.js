
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"></meta>
        <title>Google Pay</title>
        
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"></meta>
        <meta name="robots" content="noindex, nofollow"></meta>
        <meta name="googlebot" content="noindex, nofollow"></meta>
        <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
        <script
         type="text/javascript"
         src="/js/lib/dummy.js"    
        ></script>
        <link rel="stylesheet" type="text/css" href="/css/result-light.css"></link>
        <style id="compiled-css" type="text/css"></style>

        <script type="text/javascript"
        
         const baseRequest = {
             apiVersion: 2,
             apiVersionMinor: 0
            };

         const allowedCardNetworks = ["AMEX", "DISCOVER", "INTERAC", "JCB", "MASTERCARD", "VISA"];
         const allowedCardAuthMethods = ["PAN_ONLY", "CRYPTOGRAM_3DS"];
        
         /** const tokenizationSpecification = {
             "type": "DIRECT",
             "parameters": {
                 "protocolVersion": "ECv2",
                 "publicKey": "AIzaSyCRq4xiasSjvfLYwj7B_o-MWZqHL3082gY"
                 }
             }
         */
        
         const tokenizationSpecification = {
         type: 'PAYMENT_GATEWAY',
         parameters: {
                 'gateway': 'example',
                 'gatewayMerchantId': 'exampleGatewayMerchantId'
                }   
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
         let paymentsClient = null;
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
                } ;
             return paymentDataRequest;
            }

         function getGooglePaymentsClient() {
             if ( paymentsClient === null ) {
                 paymentsClient = new google.payments.api.PaymentsClient({environment: 'TEST'});
                }
             return paymentsClient;
            }

         function onGooglePayLoaded() {
             const paymentsClient = getGooglePaymentsClient();
             paymentsClient.isReadyToPay(getGoogleIsReadyToPayRequest())
             .then(function(response) {
             if (response.result) {
                 addGooglePayButton();
                 // @todo prefetch payment data to improve performance after confirming site functionality
                 // prefetchGooglePaymentData();
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
                     currencyCode: 'BRL',
                     totalPriceStatus: 'FINAL',
                     // set to cart total
                     totalPrice: '1.00'
                    };
                }

         function prefetchGooglePaymentData() {
             const paymentDataRequest = getGooglePaymentDataRequest();
             // transactionInfo must be set but does not affect cache
             paymentDataRequest.transactionInfo = {
                 totalPriceStatus: 'NOT_CURRENTLY_KNOWN',
                 currencyCode: 'BRL'
                };
             const paymentsClient = getGooglePaymentsClient();
             paymentsClient.prefetchPaymentData(paymentDataRequest);
            }

         function onGooglePaymentButtonClicked() {
             const paymentDataRequest = getGooglePaymentDataRequest();
             paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
             const paymentsClient = getGooglePaymentsClient();
             paymentsClient.loadPaymentData(paymentDataRequest)
             .then(function(paymentData) {
                     // handle the response
                     processPayment(paymentData);
                })
             .catch(function(err) {
                 // show error in developer console for debugging
                 console.error(err);
                });
            }

         function processPayment(paymentData) {
             paymentToken = paymentData.paymentMethodData.tokenizationData.token;
            }
        /script>
    </head>

    <body>
        <div id="container"></div>
        <script async
         src="https://pay.google.com/gp/p/js/pay.js"
         onload="onGooglePayLoaded()">
        </script>

        <script>
            if(window.parent && window.parent.parent){
             window.parent.parent.postMessage(["resultsFrame", {
                 height: document.body.getBoundingClientRect().height,
                 slug: "sp2mvuro"
                }], "*")
            }
            window.name = "result"
        </script>
    </body>
</html>
