# Release notes edition 3.3.3

Release date: 10th October 2024  
Version: v3

Here's the latest summary of what’s new and improved in Zudello, as well as what was resolved in the latest release.

# New and improved

### Supplier, customer and employee default document types

Code documents faster than ever, by configuring the default document type that applies when you link specific suppliers, customers, or employees to a transaction.

You can configure default document types for different submodules. For example, you might receive inventory invoices from some suppliers and service invoices from others, but treat all suppliers' credit notes the same.

We extract default document types as part of the extraction process. Importantly, we won't apply default document types when you manually match suppliers, customers, or employees to a transaction, or when an automation sets them after the extraction process has already finished.

See [Item default coding](../business-rules/item-default-coding.md) or [Supplier default coding](../business-rules/supplier-default-coding.md) for more. 

### Allocations - any line to any line matching

Zudello's [two-way and three-way matching](../purchasing-module/understanding-two-way-and-three-way-matching.md) plays an integral role in ensuring compliance and accuracy across the procurement lifecycle. 

Previously, when allocating documents (e.g. matching an invoice to a purchase order), our intelligent engine would match the lines of each document based on either stock code or description. This works well for inventory and stock-based documents, but meant that service or non-stock documents had to be manually allocated line-by-line. 

We have now expanded our engine to allow allocation on an **any line to any line** basis, allowing you to easily allocate any two transactions, even where the number of lines do not match.

When this option is enabled and a transaction is allocated (e.g. an invoice is allocated to a purchase order), lines will be allocated from top-to-bottom, until either all lines are matched or the matched transaction (in this case the purchase order) is fully consumed. 

Please contact Zudello Support to discuss enabling this feature for your team.

### Approvals - DOA based on document total

To increase the security and flexibility of approval flows, you now have the option to base each DOA approval decision on either of the following comparisons:

- The sum of applicable transaction lines **vs** the user user group's limit  
    OR
- The document total **vs** the user user group's limit

Please contact Zudello Support to discuss enabling this feature for your team.

### Importing - Item Alternatives

Zudello's Item Alternatives feature removes the frustration of updating item codes, line-by-line, when your supplier uses different stock codes than you do. Instead of manually updating item codes, you can train Zudello to automatically swap out your suppliers stock codes for your corresponding item codes. 

Previously, Item Alternatives were updated one-by-one via the item card. 

We have now enabled bulk importing of Item alternatives. When uploading item alternative imports users need to select:
- Module: **Inventory** 
- Submodule: **Catalogue** 
- **Item Alternative**

![](../images/image%20(29).png)

The following fields are currently available when creating Item Alternatives (* denotes a mandatory field):

- Item*
    - The Catalogue Item you want to lookup and link to the Transaction Line (i.e. _**your item code**_)
    - Can be imported using:
        - UUID
        - External ID
        - SKU  
          
		![](../images/image%20(31).png)

- Supplier / Customer
    - The Supplier / Customer the Item Alternative relates to. This allows you to link the same Catalogue Item if Suppliers / Customer refer to them by different codes. Can be left blank if the rule is generic i.e. the SKU is 'FREIGHT'
    - Can be imported using:
        - UUID
        - External ID
        - Code  
          
		![](../images/image%20(30).png)
		
- SKU*
    - The extracted code that you want to lookup and convert into the Linked Item (i.e. _**the supplier's/customer's item code**_)

Please reach out to your Organisation Administrator to discuss importing Item Alternatives for your team. 

# Have some ideas?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.