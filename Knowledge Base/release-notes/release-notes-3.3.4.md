# Release notes edition 3.3.4

Release date: 17 October 2024  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

# New and improved

### Allocations - custom field autofilling

Zudello's autofill feature allows you to process transactions faster than ever by autofilling coding from linked transactions (e.g. autofilling invoice line coding from the allocated PO lines).

Previously, this applied only to standard fields, and you needed to code custom fields manually on all transactions. We've now expanded the autofill feature to support custom fields, ensuring that you can copy all coding through the purchasing flow.

If you'd like to check that this feature is enabled for your team, please contact Zudello Support. 

### Supplier statement extraction

Zudello's LLM pipeline now supports the extraction and classification of supplier statements. If you or your suppliers email statements into the purchasing module, we'll automatically recognise them as statements and route them to the correct submodule.

If you need guidance on using Zudello's statement reconciliation feature, please contact Zudello Support. 

### Transaction shipping addresses

For customers using Zudello's LLM pipeline, we can now extract shipping addresses from documents and save them against the transaction.

Zudello extracts both shipping and billing addresses from documents. Once extracted, we apply the following rules to determine which address to use for the transaction:

| Shipping address extracted? | Billing address extracted? | Address applied to transaction |
| --------------------------- | -------------------------- | ------------------------------ |
| Yes                         | Yes                        | **Shipping** address applied   |
| Yes                         | No                         | **Shipping** address applied   |
| No                          | Yes                        | **Billing** address applied    |

# Resolutions

### Document classification improvements

Some customers whose teams use the LLM pipeline found that a small number of documents were getting stuck in "Scanning" status after being uploaded. This issue primarily affected statements and unsupported documents (such as images, letters, and other documents unrelated to purchasing or payables).

We've released improvements to correctly route these documents to the "Unclassified" submodule, where you can then classify them manually or delete them.

### Navigating through documents in table view

Previously, when viewing documents in the table view, you had to click out and in to move between documents.

We've now added buttons within the invoice modal to let you move to the previous or next document when available.

# Have some ideas?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.