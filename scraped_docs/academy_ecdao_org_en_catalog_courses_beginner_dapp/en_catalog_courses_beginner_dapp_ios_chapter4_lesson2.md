# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter4/lesson2

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Course Overview](/en/catalog/courses/beginner-dapp-ios)

1. Basic Concepts

[1.1 Understanding Blockchain Concepts](/en/catalog/courses/beginner-dapp-ios/chapter1/lesson1)[1.2 Exploring the Flow Blockchain & Cadence](/en/catalog/courses/beginner-dapp-ios/chapter1/lesson2)

2. Learning Swift (iOS) Development

[2.1 Creating our Mobile (iOS) DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson1)[2.2 Learning Frontend Code](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson2)[2.3 Adding Interactivity To Our DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson3)[2.4 Finishing the Skeleton](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson4)

3. Cadence Development

[3.1 Our First Smart Contract](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson1)[3.2 Transactions and Scripts](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson2)[3.3 Bringing Cadence to our DApp & Deploying our Contract](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson3)

4. Learn FCL

[4.1 Connecting the Blockchain](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson1)[4.2 Integrating WalletConnect and Lilco Wallet](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson2)[4.3 Running a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson3)[4.4 Passing in Arguments to a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson4)[4.5 Finishing the Skeleton](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson5)

Course Overview

[Catalog](/en/catalog)
[Course](/en/catalog/courses/beginner-dapp-ios)
Beginner Dapp Ios

# Chapter 4 Lesson 2 - Integrating WalletConnect and Lilco Wallet

> This lesson is optional but highly recommendedâ¦ both for the sake of user experience and so that you can be sure a self custody wallet is available for your end users.

> Unfortunately, it is currently not possible to download apps from the App Store onto the simulator. Because of this you will need a physical iOS device connected to your Mac.

Lilco Mobile uses a communication protocol called WalletConnect to enable easy communication between web/mobile DApps and mobile wallets. FCL also includes a âDiscovery Pluginâ allowing you to communicate with the protocol.

## Setup Lilico Mobile Wallet

You need to have Lilico Mobile Wallet installed on your iOS device and configured for Development use. If you havenât done this before, jump over to my tutorial: [Setting Up Lilico Wallet For Development](https://academy.ecdao.org/en/catalog/tutorials/setting-up-lilico-wallet-for-development)

## Create WalletConnect Account

First, we need to create a WalletConnect account. Head to <https://walletconnect.com> in your browser and click the `Dashboard` button.

![](https://i.imgur.com/i6pDsCal.png)

For the sake of this course, I am going to use the same disposable email address I used for Blocto Wallet, but you can also a WalletConnect compatible wallet from another chain such as Ethereum (most major wallets will support it). Unfortunately Lilico Mobile doesnât seem to work with the WalletConnect portal itself ð¢.

Once you have created an account and logged in, select `New Project` in the upper right-hand corner. Give your project a name then click `Create`

![](https://i.imgur.com/z2kyMb9l.png)
![](https://i.imgur.com/HSks19ml.png)

Head over to the `Explorer` tab and fill out the form as shown in the images below, then the `Save` button.

> Note that WalletConnect requires a large logo file (atleast 500x500) so I stole this awesome avatar from the Academy filesâ¦ <https://academy.ecdao.org/new-avatar.png>

![](https://i.imgur.com/vqY6zsv.png)
![](https://i.imgur.com/bJKf27F.png)
![](https://i.imgur.com/fJjIwi2.png)
![](https://i.imgur.com/yCNLBYC.png)
![](https://i.imgur.com/SdQd9ym.png)

Head back to the `Settings` tab and copy your `Project ID`, save this somewhere as you will need it in a later step.

![](https://i.imgur.com/QRtLeGk.png)

## Setup the WalletConnect Plugin

Add the following `WalletConnectConfig` about the `metadata` property in the `setup()` function.

swift

```
		
			let walletConnect = FCL.Metadata.WalletConnectConfig(urlScheme: "emeraldDApp://", projectID: "485264ff93ea1a0e78e96a740c1e775d")
		 
	
```

Then update the `metadata` property like so:

swift

```
		
			let metadata = FCL.Metadata(appName: "Emerald DApp!",
                                    appDescription: "EmeraldDApp for Emerald Academy",
                                    appIcon: URL(string: "https://academy.ecdao.org/ea-logo.png")!,
                                    location: URL(string: "https://academy.ecdao.org/")!,
                                    accountProof: accountProof,
                                    walletConnectConfig: walletConnect)
		 
	
```

## Running The DApp On Your iOS Device

First, you need to ensure Developer Mode is enabled on your iOS Device. If you connect an iOS, visionOS, or watchOS device with Developer Mode disabled to your Mac, the Xcode scheme selectorâs destination list shows it as an âUnavailable Deviceâ.

![](https://docs-assets.developer.apple.com/published/98d92a626934d5dd4a0941e7dae333c2/enabling-developer-mode-on-a-device-01~dark@2x.png)

Running your app on the device requires that you enable Developer Mode. On your iOS device, open Settings > Privacy & Security, scroll down to the Developer Mode list item and navigate into it. On a watchOS device that you use for development, go to Settings > Privacy > Developer Mode. To toggle Developer mode, use the Developer Mode switch.

![](https://docs-assets.developer.apple.com/published/72b149b975624bfaf5f6fb577655b200/enabling-developer-mode-on-a-device-03~dark@2x.png)

Tap the switch to enable Developer Mode. After you do so, Settings presents an alert to warn you that Developer Mode reduces the security of your device. To continue enabling Developer Mode, tap the alertâs Restart button.

After the device restarts and you unlock it, the device shows an alert confirming that you want to enable Developer Mode. To acknowledge the reduction in security protection in exchange for allowing Xcode and other tools to execute code, tap Turn On, and enter your device passcode when prompted.

At this point, your device is ready to install and run apps from Xcode. After you have enabled Developer Mode the first time, Xcode doesnât ask again unless you disable Developer Mode or you restore the device. You can Build and Run from Xcode without further prompts to enable Developer Mode.

Select your iOS device from the scheme selector then hit the play button to run our DApp on the device

![](https://i.imgur.com/UZKe84P.png)

This time when you sign in, select Lilico, if everything is working properly Lilico Moible should open automatically. Once the Auth screen loads, select Approve. In theory, you should automatically be directed back to your DApp, however, in practice sometimes the routing just doesnât workâ¦ you can manually switch back to your DApp at any time after selecting approve.

![](https://i.imgur.com/UZKe84P.png)

## Quests

Weâve got a lot to cover in lesson 3, your Quest for today is to go back over any pieces you may have struggled with up until this point. Ask any questions you might have in Discord.

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter4/lesson2.md)

[Connecting the Blockchain](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson1)
[Running a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson3)



[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow

##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)


##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)


##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)

[Join the community](https://discord.gg/emerald-city-906264258189332541)