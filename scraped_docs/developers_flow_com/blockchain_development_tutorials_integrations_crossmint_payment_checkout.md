# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/crossmint/payment-checkout

Payment Checkout Integration | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

                      + [Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)+ [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)

                          - [Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)- [Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)- [Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)- [Crossmint Smart Wallets](/blockchain-development-tutorials/integrations/crossmint/smart-wallets)

* * [Third-Party Integrations](/blockchain-development-tutorials/integrations)* [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)* Payment Checkout Integration

On this page

# Payment checkout integration guide

Enable seamless fiat and cryptocurrency payments for your Flow assets. Crossmint's checkout solution supports credit cards, Apple Pay, Google Pay, and cross-chain crypto payments, allowing users to buy Flow NFTs and tokens without holding FLOW tokens.

## Overview[​](#overview "Direct link to Overview")

Crossmint Checkout supports multiple payment methods and handles complex blockchain interactions behind the scenes, which eliminates payment friction. Users can buy your Flow assets with familiar payment methods.

> **Key benefits:**
>
> * **No wallet required** - guest checkout available.
> * **Global coverage** - 197 countries supported.
> * **No buyer KYC** for most transactions.
> * **Cross-chain payments** - Pay with any crypto, receive on Flow.

## What you'll build[​](#what-youll-build "Direct link to What you'll build")

You'll integrate checkout functionality that activates:

* Credit card payments for Flow NFTs and tokens.
* Apple Pay and Google Pay support.
* Cross-chain crypto payments.
* Guest checkout (no wallet required).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Crossmint account with checkout activated.
* Flow collection created or imported.
* Basic understanding of payment flows.
* For production: KYB verification completed.

## Step 1: Collection setup[​](#step-1-collection-setup "Direct link to Step 1: Collection setup")

### Create or import collection[​](#create-or-import-collection "Direct link to Create or import collection")

**Option A: create new collection**

1. Go to [Crossmint Console](https://staging.crossmint.com) > **Collections**.
2. Click **Create Collection**.
3. Choose **Flow** blockchain.
4. Configure collection settings:
   * Network: Flow Testnet/Mainnet
   * Contract type: ERC-721 (EVM) or Cadence NFT
   * Pricing in USD or FLOW
   * Maximum supply and metadata

**Option B: Import current collection**

`_11

// Import existing Flow contract

_11

const collection = await crossmint.collections.import({

_11

blockchain: "flow",

_11

contractAddress: "0x1234567890abcdef", // Your contract address

_11

type: "erc-721", // or "cadence-nft"

_11

metadata: {

_11

name: "My Flow Collection",

_11

symbol: "MFC",

_11

description: "Amazing NFTs on Flow"

_11

}

_11

});`

### Configure payment settings[​](#configure-payment-settings "Direct link to Configure payment settings")

In your collection settings:

1. Go to **Payments > Settings**.
2. Choose fee structure:
   * **Buyer pays fees**: user pays NFT price + fees.
   * **Seller pays fees**: user pays exact price, you pay fees.
3. Set accepted payment methods.
4. Configure webhooks for order updates.

## Step 2: Hosted Checkout Integration[​](#step-2-hosted-checkout-integration "Direct link to Step 2: Hosted Checkout Integration")

The fastest way to get started - Crossmint hosts the entire checkout experience.

### Basic hosted checkout[​](#basic-hosted-checkout "Direct link to Basic hosted checkout")

`` _39

// src/components/HostedCheckout.jsx

_39

import React from 'react';

_39

_39

export function HostedCheckout({ collectionId, nftId, onSuccess }) {

_39

const openCheckout = () => {

_39

const checkoutUrl = `https://www.crossmint.com/checkout?` +

_39

`clientId=${process.env.REACT_APP_CROSSMINT_CLIENT_ID}&` +

_39

`collectionId=${collectionId}&` +

_39

`templateId=${nftId}&` +

_39

`successCallbackURL=${encodeURIComponent(window.location.origin + '/success')}&` +

_39

`cancelCallbackURL=${encodeURIComponent(window.location.origin + '/cancel')}`;

_39

_39

// Open in new window

_39

const popup = window.open(

_39

checkoutUrl,

_39

'crossmint-checkout',

_39

'width=500,height=700,scrollbars=yes,resizable=yes'

_39

);

_39

_39

// Listen for completion

_39

const checkClosed = setInterval(() => {

_39

if (popup.closed) {

_39

clearInterval(checkClosed);

_39

onSuccess?.();

_39

}

_39

}, 1000);

_39

};

_39

_39

return (

_39

<div className="hosted-checkout">

_39

<button

_39

onClick={openCheckout}

_39

className="checkout-btn primary"

_39

>

_39

🛒 Buy with Crossmint

_39

</button>

_39

</div>

_39

);

_39

} ``

### Advanced hosted checkout[​](#advanced-hosted-checkout "Direct link to Advanced hosted checkout")

`` _42

// More control over hosted checkout

_42

export function AdvancedHostedCheckout({

_42

collectionId,

_42

nftId,

_42

customization,

_42

onSuccess,

_42

onError

_42

}) {

_42

const openCheckout = () => {

_42

const params = new URLSearchParams({

_42

clientId: process.env.REACT_APP_CROSSMINT_CLIENT_ID,

_42

collectionId,

_42

templateId: nftId,

_42

// Customization options

_42

theme: customization.theme || 'dark',

_42

accentColor: customization.accentColor || '#00D4AA',

_42

backgroundColor: customization.backgroundColor || '#1A1A1A',

_42

// Callback URLs

_42

successCallbackURL: `${window.location.origin}/checkout/success`,

_42

cancelCallbackURL: `${window.location.origin}/checkout/cancel`,

_42

// Payment options

_42

enableApplePay: 'true',

_42

enableGooglePay: 'true',

_42

enableCrypto: 'true',

_42

// User experience

_42

showConnectWallet: 'true',

_42

collectEmail: 'true'

_42

});

_42

_42

window.open(

_42

`https://www.crossmint.com/checkout?${params}`,

_42

'crossmint-checkout',

_42

'width=500,height=700,scrollbars=yes,resizable=yes'

_42

);

_42

};

_42

_42

return (

_42

<button onClick={openCheckout} className="crossmint-checkout-btn">

_42

Buy Now - Credit Card or Crypto

_42

</button>

_42

);

_42

} ``

---

## Step 3: embedded checkout integration[​](#step-3-embedded-checkout-integration "Direct link to Step 3: embedded checkout integration")

Embed checkout directly in your application with full UI control.

### Basic embedded checkout[​](#basic-embedded-checkout "Direct link to Basic embedded checkout")

`_44

// src/components/EmbeddedCheckout.jsx

_44

import React from 'react';

_44

import { CrossmintPayButton } from '@crossmint/embed-react';

_44

_44

export function EmbeddedCheckout({ collectionId, nftId, recipient }) {

_44

return (

_44

<div className="embedded-checkout">

_44

<CrossmintPayButton

_44

collectionId={collectionId}

_44

projectId={process.env.REACT_APP_CROSSMINT_PROJECT_ID}

_44

mintConfig={{

_44

type: "erc-721",

_44

quantity: 1,

_44

...(nftId && { templateId: nftId })

_44

}}

_44

recipient={{

_44

email: recipient?.email,

_44

walletAddress: recipient?.walletAddress

_44

}}

_44

checkoutProps={{

_44

paymentMethods: ['fiat', 'ETH', 'SOL', 'MATIC'],

_44

showWalletOptions: true,

_44

theme: 'dark'

_44

}}

_44

onEvent={(event) => {

_44

console.log('Checkout event:', event);

_44

_44

switch (event.type) {

_44

case 'payment:process.succeeded':

_44

console.log('✅ Payment succeeded:', event.payload);

_44

break;

_44

case 'payment:process.failed':

_44

console.log('❌ Payment failed:', event.payload);

_44

break;

_44

case 'ui:payment-method.selected':

_44

console.log('Payment method selected:', event.payload);

_44

break;

_44

}

_44

}}

_44

environment="staging" // or "production"

_44

/>

_44

</div>

_44

);

_44

}`

### Custom styled embedded checkout[​](#custom-styled-embedded-checkout "Direct link to Custom styled embedded checkout")

`_73

// Advanced embedded checkout with custom styling

_73

export function CustomEmbeddedCheckout({

_73

collectionId,

_73

nftId,

_73

pricing,

_73

onCheckoutComplete

_73

}) {

_73

return (

_73

<div className="custom-checkout-container">

_73

<div className="checkout-header">

_73

<h3>Complete Your Purchase</h3>

_73

<div className="price-display">

_73

<span className="price">${pricing.usd}</span>

_73

<span className="price-alt">≈ {pricing.flow} FLOW</span>

_73

</div>

_73

</div>

_73

_73

<CrossmintPayButton

_73

collectionId={collectionId}

_73

projectId={process.env.REACT_APP_CROSSMINT_PROJECT_ID}

_73

mintConfig={{

_73

type: "erc-721",

_73

quantity: 1,

_73

templateId: nftId,

_73

totalPrice: pricing.usd.toString()

_73

}}

_73

checkoutProps={{

_73

paymentMethods: [

_73

'fiat', // Credit cards

_73

'ETH', // Ethereum

_73

'MATIC', // Polygon

_73

'SOL', // Solana

_73

'BTC', // Bitcoin

_73

'FLOW' // Flow native

_73

],

_73

theme: {

_73

colors: {

_73

primary: '#00D4AA',

_73

background: '#FFFFFF',

_73

textPrimary: '#1A1A1A',

_73

textSecondary: '#6B7280'

_73

},

_73

borderRadius: '8px',

_73

fontFamily: 'Inter, sans-serif'

_73

},

_73

locale: 'en-US',

_73

currency: 'USD'

_73

}}

_73

onEvent={handleCheckoutEvent}

_73

className="custom-crossmint-button"

_73

/>

_73

</div>

_73

);

_73

_73

function handleCheckoutEvent(event) {

_73

switch (event.type) {

_73

case 'payment:process.succeeded':

_73

onCheckoutComplete?.({

_73

success: true,

_73

transactionId: event.payload.transactionId,

_73

nftId: event.payload.nftId

_73

});

_73

break;

_73

_73

case 'payment:process.failed':

_73

onCheckoutComplete?.({

_73

success: false,

_73

error: event.payload.error

_73

});

_73

break;

_73

}

_73

}

_73

}`

---

## Step 4: Headless Checkout Integration[​](#step-4-headless-checkout-integration "Direct link to Step 4: Headless Checkout Integration")

For maximum customization, use the headless API to build completely custom checkout flows.

### Order creation service[​](#order-creation-service "Direct link to Order creation service")

`` _136

// src/services/checkoutService.ts

_136

import { CrossmintSDK } from '@crossmint/client-sdk';

_136

_136

const crossmint = new CrossmintSDK({

_136

apiKey: process.env.CROSSMINT_API_KEY!,

_136

environment: 'staging'

_136

});

_136

_136

export interface CheckoutOrder {

_136

id: string;

_136

status: string;

_136

clientSecret: string;

_136

paymentIntent?: any;

_136

}

_136

_136

export class CheckoutService {

_136

// Create fiat payment order

_136

async createFiatOrder(params: {

_136

collectionId: string;

_136

nftId?: string;

_136

recipientEmail: string;

_136

recipientWallet?: string;

_136

quantity?: number;

_136

}): Promise<CheckoutOrder> {

_136

try {

_136

const order = await crossmint.orders.create({

_136

payment: {

_136

method: "fiat",

_136

currency: "usd"

_136

},

_136

lineItems: [{

_136

collectionLocator: `crossmint:${params.collectionId}`,

_136

...(params.nftId && { templateId: params.nftId }),

_136

quantity: params.quantity || 1

_136

}],

_136

recipient: {

_136

email: params.recipientEmail,

_136

...(params.recipientWallet && { walletAddress: params.recipientWallet })

_136

},

_136

metadata: {

_136

source: 'custom_checkout'

_136

}

_136

});

_136

_136

return {

_136

id: order.id,

_136

status: order.status,

_136

clientSecret: order.clientSecret,

_136

paymentIntent: order.paymentIntent

_136

};

_136

} catch (error) {

_136

console.error('❌ Order creation failed:', error);

_136

throw error;

_136

}

_136

}

_136

_136

// Create crypto payment order

_136

async createCryptoOrder(params: {

_136

collectionId: string;

_136

nftId?: string;

_136

recipientWallet: string;

_136

paymentToken: string; // 'ETH', 'MATIC', 'SOL', etc.

_136

quantity?: number;

_136

}): Promise<CheckoutOrder> {

_136

try {

_136

const order = await crossmint.orders.create({

_136

payment: {

_136

method: "crypto",

_136

currency: params.paymentToken.toLowerCase()

_136

},

_136

lineItems: [{

_136

collectionLocator: `crossmint:${params.collectionId}`,

_136

...(params.nftId && { templateId: params.nftId }),

_136

quantity: params.quantity || 1

_136

}],

_136

recipient: {

_136

walletAddress: params.recipientWallet

_136

}

_136

});

_136

_136

return {

_136

id: order.id,

_136

status: order.status,

_136

clientSecret: order.clientSecret

_136

};

_136

} catch (error) {

_136

console.error('❌ Crypto order creation failed:', error);

_136

throw error;

_136

}

_136

}

_136

_136

// Check order status

_136

async getOrderStatus(orderId: string) {

_136

try {

_136

const order = await crossmint.orders.get(orderId);

_136

return order;

_136

} catch (error) {

_136

console.error('❌ Order status check failed:', error);

_136

throw error;

_136

}

_136

}

_136

_136

// Handle order completion

_136

async handleOrderComplete(orderId: string) {

_136

try {

_136

const order = await crossmint.orders.get(orderId);

_136

_136

if (order.status === 'succeeded') {

_136

// Order completed successfully

_136

return {

_136

success: true,

_136

nft: order.nft,

_136

transaction: order.transaction

_136

};

_136

} else if (order.status === 'failed') {

_136

// Order failed

_136

return {

_136

success: false,

_136

error: order.error

_136

};

_136

}

_136

_136

// Order still processing

_136

return {

_136

success: false,

_136

processing: true,

_136

status: order.status

_136

};

_136

} catch (error) {

_136

console.error('❌ Order completion check failed:', error);

_136

throw error;

_136

}

_136

}

_136

}

_136

_136

export const checkoutService = new CheckoutService(); ``

### Custom checkout component[​](#custom-checkout-component "Direct link to Custom checkout component")

`` _128

// src/components/CustomCheckout.tsx

_128

import React, { useState } from 'react';

_128

import { loadStripe } from '@stripe/stripe-js';

_128

import { Elements, PaymentElement, useStripe, useElements } from '@stripe/react-stripe-js';

_128

import { checkoutService } from '../services/checkoutService';

_128

_128

const stripePromise = loadStripe(process.env.REACT_APP_STRIPE_PUBLISHABLE_KEY!);

_128

_128

interface CheckoutFormProps {

_128

collectionId: string;

_128

nftId: string;

_128

onSuccess: (result: any) => void;

_128

onError: (error: any) => void;

_128

}

_128

_128

function CheckoutForm({ collectionId, nftId, onSuccess, onError }: CheckoutFormProps) {

_128

const stripe = useStripe();

_128

const elements = useElements();

_128

const [isProcessing, setIsProcessing] = useState(false);

_128

const [paymentMethod, setPaymentMethod] = useState<'fiat' | 'crypto'>('fiat');

_128

const [recipientEmail, setRecipientEmail] = useState('');

_128

_128

const handleFiatPayment = async (e: React.FormEvent) => {

_128

e.preventDefault();

_128

if (!stripe || !elements) return;

_128

_128

setIsProcessing(true);

_128

_128

try {

_128

// Create order

_128

const order = await checkoutService.createFiatOrder({

_128

collectionId,

_128

nftId,

_128

recipientEmail

_128

});

_128

_128

// Confirm payment with Stripe

_128

const { error, paymentIntent } = await stripe.confirmPayment({

_128

elements,

_128

clientSecret: order.clientSecret,

_128

confirmParams: {

_128

return_url: `${window.location.origin}/checkout/complete`

_128

}

_128

});

_128

_128

if (error) {

_128

onError(error);

_128

} else if (paymentIntent?.status === 'succeeded') {

_128

// Poll for NFT delivery

_128

const result = await checkoutService.handleOrderComplete(order.id);

_128

onSuccess(result);

_128

}

_128

} catch (error) {

_128

onError(error);

_128

} finally {

_128

setIsProcessing(false);

_128

}

_128

};

_128

_128

const handleCryptoPayment = async () => {

_128

// Implement crypto payment flow

_128

// This would integrate with wallet providers

_128

console.log('Crypto payment not implemented in this example');

_128

};

_128

_128

return (

_128

<div className="custom-checkout-form">

_128

<div className="payment-method-selector">

_128

<button

_128

className={paymentMethod === 'fiat' ? 'active' : ''}

_128

onClick={() => setPaymentMethod('fiat')}

_128

>

_128

💳 Card / Apple Pay

_128

</button>

_128

<button

_128

className={paymentMethod === 'crypto' ? 'active' : ''}

_128

onClick={() => setPaymentMethod('crypto')}

_128

>

_128

🪙 Crypto

_128

</button>

_128

</div>

_128

_128

{paymentMethod === 'fiat' ? (

_128

<form onSubmit={handleFiatPayment} className="fiat-payment-form">

_128

<div className="form-group">

_128

<label>Email Address</label>

_128

<input

_128

type="email"

_128

value={recipientEmail}

_128

onChange={(e) => setRecipientEmail(e.target.value)}

_128

required

_128

placeholder="your@email.com"

_128

/>

_128

</div>

_128

_128

<div className="payment-element-container">

_128

<PaymentElement />

_128

</div>

_128

_128

<button

_128

type="submit"

_128

disabled={!stripe || isProcessing}

_128

className="pay-button"

_128

>

_128

{isProcessing ? 'Processing...' : 'Complete Purchase'}

_128

</button>

_128

</form>

_128

) : (

_128

<div className="crypto-payment-form">

_128

<div className="crypto-options">

_128

<button onClick={handleCryptoPayment}>Pay with ETH</button>

_128

<button onClick={handleCryptoPayment}>Pay with MATIC</button>

_128

<button onClick={handleCryptoPayment}>Pay with SOL</button>

_128

<button onClick={handleCryptoPayment}>Pay with FLOW</button>

_128

</div>

_128

</div>

_128

)}

_128

</div>

_128

);

_128

}

_128

_128

export function CustomCheckout(props: CheckoutFormProps) {

_128

return (

_128

<Elements stripe={stripePromise}>

_128

<CheckoutForm {...props} />

_128

</Elements>

_128

);

_128

} ``

---

## Step 5: webhook integration[​](#step-5-webhook-integration "Direct link to Step 5: webhook integration")

Set up webhooks to handle order status updates in real-time.

### Webhook handler[​](#webhook-handler "Direct link to Webhook handler")

`_63

// src/api/webhooks/crossmint.ts (Next.js API route example)

_63

import { NextApiRequest, NextApiResponse } from 'next';

_63

import crypto from 'crypto';

_63

_63

export default function handler(req: NextApiRequest, res: NextApiResponse) {

_63

if (req.method !== 'POST') {

_63

return res.status(405).json({ error: 'Method not allowed' });

_63

}

_63

_63

// Verify webhook signature

_63

const signature = req.headers['x-crossmint-signature'] as string;

_63

const payload = JSON.stringify(req.body);

_63

const expectedSignature = crypto

_63

.createHmac('sha256', process.env.CROSSMINT_WEBHOOK_SECRET!)

_63

.update(payload)

_63

.digest('hex');

_63

_63

if (signature !== expectedSignature) {

_63

return res.status(401).json({ error: 'Invalid signature' });

_63

}

_63

_63

const event = req.body;

_63

_63

switch (event.type) {

_63

case 'order.succeeded':

_63

handleOrderSucceeded(event.data);

_63

break;

_63

case 'order.failed':

_63

handleOrderFailed(event.data);

_63

break;

_63

case 'order.delivered':

_63

handleOrderDelivered(event.data);

_63

break;

_63

default:

_63

console.log('Unhandled webhook event:', event.type);

_63

}

_63

_63

res.status(200).json({ received: true });

_63

}

_63

_63

async function handleOrderSucceeded(orderData: any) {

_63

console.log('✅ Order succeeded:', orderData.orderId);

_63

_63

// Update your database

_63

// Send confirmation email

_63

// Trigger any post-purchase flows

_63

}

_63

_63

async function handleOrderFailed(orderData: any) {

_63

console.log('❌ Order failed:', orderData.orderId, orderData.error);

_63

_63

// Handle failed order

_63

// Notify user

_63

// Log for analysis

_63

}

_63

_63

async function handleOrderDelivered(orderData: any) {

_63

console.log('📦 NFT delivered:', orderData.orderId, orderData.nft);

_63

_63

// NFT successfully delivered to user

_63

// Update user's account

_63

// Send delivery confirmation

_63

}`

---

## Step 6: multi-payment method component[​](#step-6-multi-payment-method-component "Direct link to Step 6: multi-payment method component")

Create a comprehensive checkout that supports all payment methods:

`_112

// src/components/UniversalCheckout.tsx

_112

import React, { useState } from 'react';

_112

import { EmbeddedCheckout } from './EmbeddedCheckout';

_112

import { CustomCheckout } from './CustomCheckout';

_112

import { HostedCheckout } from './HostedCheckout';

_112

_112

interface UniversalCheckoutProps {

_112

collectionId: string;

_112

nftId: string;

_112

pricing: {

_112

usd: number;

_112

flow: number;

_112

};

_112

onCheckoutComplete: (result: any) => void;

_112

}

_112

_112

export function UniversalCheckout({

_112

collectionId,

_112

nftId,

_112

pricing,

_112

onCheckoutComplete

_112

}: UniversalCheckoutProps) {

_112

const [checkoutMode, setCheckoutMode] = useState<'hosted' | 'embedded' | 'custom'>('embedded');

_112

const [showPaymentMethods, setShowPaymentMethods] = useState(false);

_112

_112

return (

_112

<div className="universal-checkout">

_112

<div className="checkout-header">

_112

<h2>🛒 Purchase NFT</h2>

_112

<div className="pricing-info">

_112

<div className="price-primary">${pricing.usd}</div>

_112

<div className="price-secondary">≈ {pricing.flow} FLOW</div>

_112

</div>

_112

</div>

_112

_112

<div className="payment-methods-preview">

_112

<div className="payment-icons">

_112

<span className="payment-icon">💳</span>

_112

<span className="payment-icon">🍎</span>

_112

<span className="payment-icon">🅿️</span>

_112

<span className="payment-icon">⚡</span>

_112

<span className="payment-icon">🪙</span>

_112

</div>

_112

<p>Credit Card, Apple Pay, Google Pay, and 40+ cryptocurrencies</p>

_112

</div>

_112

_112

<div className="checkout-mode-selector">

_112

<button

_112

className={checkoutMode === 'embedded' ? 'active' : ''}

_112

onClick={() => setCheckoutMode('embedded')}

_112

>

_112

🎨 Styled Checkout

_112

</button>

_112

<button

_112

className={checkoutMode === 'hosted' ? 'active' : ''}

_112

onClick={() => setCheckoutMode('hosted')}

_112

>

_112

🚀 Quick Checkout

_112

</button>

_112

<button

_112

className={checkoutMode === 'custom' ? 'active' : ''}

_112

onClick={() => setCheckoutMode('custom')}

_112

>

_112

⚙️ Custom Checkout

_112

</button>

_112

</div>

_112

_112

<div className="checkout-container">

_112

{checkoutMode === 'hosted' && (

_112

<HostedCheckout

_112

collectionId={collectionId}

_112

nftId={nftId}

_112

onSuccess={onCheckoutComplete}

_112

/>

_112

)}

_112

_112

{checkoutMode === 'embedded' && (

_112

<EmbeddedCheckout

_112

collectionId={collectionId}

_112

nftId={nftId}

_112

pricing={pricing}

_112

onCheckoutComplete={onCheckoutComplete}

_112

/>

_112

)}

_112

_112

{checkoutMode === 'custom' && (

_112

<CustomCheckout

_112

collectionId={collectionId}

_112

nftId={nftId}

_112

onSuccess={onCheckoutComplete}

_112

onError={(error) => console.error('Checkout error:', error)}

_112

/>

_112

)}

_112

</div>

_112

_112

<div className="checkout-benefits">

_112

<div className="benefit">

_112

<span className="benefit-icon">🔒</span>

_112

<span>Secure & trusted by Fortune 500</span>

_112

</div>

_112

<div className="benefit">

_112

<span className="benefit-icon">🌍</span>

_112

<span>Available in 197 countries</span>

_112

</div>

_112

<div className="benefit">

_112

<span className="benefit-icon">⚡</span>

_112

<span>Instant delivery to wallet</span>

_112

</div>

_112

</div>

_112

</div>

_112

);

_112

}`

## Key takeaways[​](#key-takeaways "Direct link to Key takeaways")

* **Multiple Integration Options**: hosted, embedded, or headless - choose what fits your needs.
* **Universal Payment Support**: credit cards, mobile payments, and over 40 cryptocurrencies.
* **Flow Native**: optimized for both Flow EVM and Cadence ecosystems.
* **Global Scale**: support for 197 countries with no buyer KYC.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/integrations/crossmint/payment-checkout.md)

Last updated on **Nov 12, 2025** by **cshannon1218**

[Previous

Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)[Next

Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [What you'll build](#what-youll-build)* [Prerequisites](#prerequisites)* [Step 1: Collection setup](#step-1-collection-setup)
        + [Create or import collection](#create-or-import-collection)+ [Configure payment settings](#configure-payment-settings)* [Step 2: Hosted Checkout Integration](#step-2-hosted-checkout-integration)
          + [Basic hosted checkout](#basic-hosted-checkout)+ [Advanced hosted checkout](#advanced-hosted-checkout)* [Step 3: embedded checkout integration](#step-3-embedded-checkout-integration)
            + [Basic embedded checkout](#basic-embedded-checkout)+ [Custom styled embedded checkout](#custom-styled-embedded-checkout)* [Step 4: Headless Checkout Integration](#step-4-headless-checkout-integration)
              + [Order creation service](#order-creation-service)+ [Custom checkout component](#custom-checkout-component)* [Step 5: webhook integration](#step-5-webhook-integration)
                + [Webhook handler](#webhook-handler)* [Step 6: multi-payment method component](#step-6-multi-payment-method-component)* [Key takeaways](#key-takeaways)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.