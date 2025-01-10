###### Release Date: 10th October 2024  
###### Version: v3

Here's the latest summary of what’s new and improved in Zudello, as well as what was resolved in the latest release.

# New and improved

### Supplier, Customer and Employee default document types

To make coding documents faster than ever, Zudello now allows you to configure the default Document Type that should be applied when specific Suppliers, Customers or Employees are linked to a Transaction.

Default document types can be configured for different submodules. For example, you may receive Inventory Invoices from some Suppliers and Service Invoices from others, but treat all suppliers' Credit Notes the same. 

Default Document Types will be extracted as part of the extraction process. Importantly, default document types will NOT be applied when Suppliers/Customers/Employees are manually matched to a transaction, or when they are set by an automation process after the document has been extracted.

Please contact [support@zudello.com](mailto:support@zudello.com,) to discuss enabling this feature for your team.

### Allocations - 'any line to any line' matching

Zudello's 2- and 3-way matching plays an integral role in ensuring compliance and accuracy across the procurement lifecycle. 

Previously, when allocating documents (e.g. matching an invoice to a purchase order), our intelligent engine would match the lines of each document based on either stock code or description. This works well for inventory & stock-based documents, but meant that service or non-stock documents had to be manually allocated line-by-line. 

We have now expanded our engine to allow _**allocation on an 'Any line to any line' basis**_, allowing you to easily allocate any two transactions, even where the number of lines do not match.

When this option is enabled, and a transaction is allocated (e.g. an invoice is allocated to a purchase order), lines will be allocated from top-to-bottom, until either all lines are matched or the matched transaction (in this case the purchase order) is fully consumed. 

Please contact [support@zudello.com](mailto:support@zudello.com,) to discuss enabling this feature for your team.

### Approvals - DOA based on document total

To increase the security and flexibility of approval flows, you now have the option to base each DOA approval decision on either of the following comparisons:

- The sum of applicable transaction lines **vs** the user user group's limit  
    OR
- The document total **vs** the user user group's limit

Approval setting changes can be made by contacting [support@zudello.com,](mailto:support@zudello.com,) or using the in-app support chat function. 

### Importing - Item Alternatives

Zudello's Item Alternatives feature removes the frustration of updating item codes, line-by-line, when your supplier uses different stock codes than you do. Instead of manually updating item codes, you can train Zudello to automatically swap out your suppliers stock codes for your corresponding item codes. 

Previously, Item Alternatives were updated one-by-one via the Item Card (navigate to Inventory > Catalogue).

We have now enabled _**bulk importing of Item alternatives**_. When uploading item alternatives users need to select Module: 'Inventory' > Submodule: 'Catalogue' > 'Item Alternative'

![](https://t6945052.p.clickup-attachments.com/t6945052/7e2d8433-ae7a-40ff-9d8d-ce7533564304/image.png)

The following fields are currently available when creating Item Alternatives (* denotes a mandatory field)

- Item*
    - The Catalogue Item you want to lookup and link to the Transaction Line (i.e. _**your item code**_)
    - Can be imported using:
        - UUID
        - External ID
        - SKU  
            ![](https://t6945052.p.clickup-attachments.com/t6945052/ca319edd-b98c-4242-9107-42b034296336/image.png)
- Supplier / Customer
    - The Supplier / Customer the Item Alternative relates to. This allows you to link the same Catalogue Item if Suppliers / Customer refer to them by different codes. Can be left blank if the rule is generic ie "FREIGHT"
    - Can be imported using:
        - UUID
        - External ID
        - Code  
            ![](https://t6945052.p.clickup-attachments.com/t6945052/79b9caaa-e2f7-4408-b30a-5ffc1d494b44/image.png)![](https://t6945052.p.clickup-attachments.com/t6945052/e478545f-0553-4bbb-8277-80d2f1228355/image.png)
- SKU*
    - The extracted code that you want to lookup and convert into the Linked Item (i.e. _**the supplier's/customer's item code**_)

Please reach out to your Organisation Administrator to discuss importing Item Alternatives for your team. 

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.