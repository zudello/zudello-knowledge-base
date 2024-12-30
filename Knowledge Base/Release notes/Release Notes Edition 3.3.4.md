###### Release Date: 17th October 2024  
###### Version: v3

Here's the latest summary of what’s new and improved in Zudello, as well as what was resolved in the latest release.

# New and improved

### Allocations - custom field autofilling

Zudello's autofill feature allows you to process transactions faster than ever, by autofilling coding from linked transactions (e.g. autofilling invoice line coding from the allocated PO lines).

Previously this applied only to standard fields, and custom fields needed to be coded manually on all transactions. We have now expanded the feature to support custom fields as well, ensuring that all coding can be copied through the purchasing flow. 

If you would like to check that this feature is enabled for your team, please contact [support@zudello.com](mailto:support@zudello.com,) 
### Supplier statement extraction

Zudello's LLM pipeline now supports the extraction and classification of supplier statements! 

If statements are emailed into the purchasing module, they will be recognised as statements automatically and routed to the correct submodule. 

If you need any guidance around using Zudello's statement reconciliation feature, please contact [support@zudello.com](mailto:support@zudello.com,) 

### Transaction shipping addresses

For customer's using Zudello's LLM Pipeline, shipping address on documents can now be extracted and saved against the transaction. 

Zudello will extract both shipping and billing addresses from documents. Once extracted, the following rules will determine which address is applied to the transaction:

|   |   |   |
|---|---|---|
|**Shipping Address Extracted?**|**Billing Address Extracted?**|**Address applied to Transaction**|
|Yes|Yes|_**Shipping**_ address applied|
|Yes|No|_**Shipping**_ address applied|
|No|Yes|_**Billing**_ address applied|

# Resolutions

### Document classification improvements

Some customer's whose teams use the LLM pipeline were finding that a small number of documents were getting stuck in 'Scanning' status after being uploaded. This issue was primarily affecting statements and unsupported documents (such as images, letters, and other documents unrelated to purchasing or payables).

We have released improvements to allow these documents to be correctly routed to the 'Unclassified' submodule, where they can then be classified manually by users, or deleted. 

### Navigating through documents in table view

Previously, when viewing documents in the table view, users had to click out and in to move between documents. 

We have now added buttons within the invoice modal to allow you to move to the previous or next document when available.

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.