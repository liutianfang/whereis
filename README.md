# ItemManagement

This project is a smart speaker application product design, with python sample code.

## item management in smart speaker era

Household item management is a very useful application。 Some of us occasionally will not find things, keys, wallets, insurance policies, spare batteries, clothes saved in the season, and so on, and others will not find it everyday thing. For a long time, there has been a desire for software that can help us document where items are. However, the convenience of the operation led to even a simple mobile app, we all feel the operation is complicated, requiring too many steps: take out the phone, unlock, find the software, search for the item name ...

The emergence of smart speakers, the use of this function can be very simple to achieve:

	I can tell smart speakers: (wake-up words), I put the spare car key in the study desk drawer

	It answers: I have noticed that the spare car key is in the desk drawer

	When looking for items, tell smart speaker: (wake-up words), where is the spare car key?

	It answers: The spare car key is in the study desk drawer



## Product form
Item Management: Household, office items management;

Children's games: find something to help children call the things' names, learn the pronunciation of the item (incorrect pronunciation is not correct answer), the location of the relationship (on the table, behind the sofa, etc.

## Why I do not develop/run this service / product?
This service / product is easy to use but also needs app support, personnel nickname management , multi-level location management, storage of item location. The realization of these functions, only can be in the smart speakers native app, other app no chance to promote to the user because:
1. This service can not have income, there is no promotion costs.
2. In addition this service also requires online server and storage devices, these services also need to cost
3. However, this service and its extended functionality can be a typical application for smart speakers because it is too handy

So, if you want to use this feature, tell manufacturers of smart speakers, Amazon, Google, Apple, Microsoft, let them integrate this feature into their products.

## the term
### action: The basic actions / functions of item management are:
    Items are placed in a location, "put" in code
    Where is the item? "whereis" in code

Actions have templates to separate variables in voice command (experimental code is not written as a regular template). And according to the back-end database storage control methods, and error handling.

### Key words:
Action corresponds to a number of key words, key words of action "place to" is "put" in English . Item searching Keywords in English are  "where is", "where are"

### variable
The main variables are the item name and location.


## totype function
1. Use keywords to identify action
2. delete modal particle in Chinese
3. Chinese / English basic variable identification

with the action, variables, follow-up processing is very traditional technology, save / query the database, assemble the return text.

## Test Results

command is the input voice command, action is action, position is the position, item is the item name


	command   i put mummy's key on the table
	language= en
	action   put
	posotion : on the table
	item :  mummy's key
	________________________________
	command   where is mummy's key
	language= en
	action   whereis
	item : mummy's key
	________________________________
	command   我把妈妈的钥匙放在桌子上
	language= zh
	action   put
	item : 妈妈的钥匙
	posotion : 桌子上
	________________________________
	command   妈妈的钥匙在哪里
	language= zh
	action   whereis
	item : 妈妈的钥匙
	________________________________
  
  
## About speech recognition

I tested the voice input on phone. kedaxunfei input method of voice input Chinese, very accurately identify; English recognition is not very accurate, the use of Google's voice input is also wrong, I may not pronunciation standard , Self-deprecating about it


## A little intelligence

In the item name, there are maybe some relative descriptors processing to be handled specially, such as today's newspaper, this month's magazine, this year's insurance policy, the absolute value of these descriptors and speaking time related to search after a while, if Searching with these relativity descriptors can not search for the correct item. So when entering, you need to get the relative descriptor absolute value and save it. Search is also the same name for the goods to do the same.

Also test the smart assistant / search engine, in addition to "today's weather", other time related words are not dealt with, such as February 2018 search for "last year's event," in the three search engines (bing, baidu, google) get the result shown, huh, huh
  
