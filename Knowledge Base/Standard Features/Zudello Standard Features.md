# Inboxes
#### Customisable inboxes and defaults
Ensure your documents are extracted as soon as possible by setting up customised Zudello inboxes. 
Zudello's inboxes allow you to configure as many inboxes as required by your business. For each inbox, you can customise the following:
- The local name (the part of the email address before the **@**)
- The display name within Zudello, to allow you to easily identify inboxes
- The **reply to** address
- The Zudello module that the inbox relates to
- The default subsidiary and location to apply to all documents sent to the inbox  
# Document functions 

The following functions are available only for document types specified in your organisation's solution design. 
> Some functions may not apply to all modules, submodules or document types.

> All functions are subject to user permissions. To confirm which functions you can perform, please contact your Organisation Administrator. 

-  Statuses
	- Rename, reorder, and choose the colour of Zudello statuses to ensure they are aligned with your business's terminology.
	  
- Filtering
	- Quickly filter documents by supplier/customer, location, subsidiary, or assigned User.
	- For more complex filters, Zudello's Advanced Filter enables you to filter by almost any field on documents
	- If you know the details of the document, Zudello's search bar allows you to search by Document Number, Reference Field, or Supplier Name
	  
- Multiple document views 
	- Zudello offers three view options - List view, Table view and Board view. 
	- Each can be customised and sorted to suit your specific role. 
	- Select Me Mode to quickly filter down to only those documents to which you've been assigned. 
	  
- Tagging
	- Instantly categorise documents by adding custom tags. Tags can be created and customised to suit your business. 
	- Documents can be filtered by tag to ensure you see only the documents you need to. 

- Document field settings
	- Choose which fields on documents are required and which are optional
	- Add filters to fields to include or exclude certain records (not all records can be filtered, and not all record values can be filtered upon)
	- Add validation rules to ensure values entered meet certain criteria (min length, max length, format, *required if* rules)
	- Configure dependencies between fields to simplify coding (dependencies are not available between all fields, and may need to be manually configured by users)
- Downloading documents
	- Download the original file for exacted documents.
	- Documents can be downloaded individually or in bulk. Bulk documents will be made available for download within the **Exports** section
	  
- Creating documents 
	- Creation of documents/records is available in all available submodules.
> NOTE: creating documents may count towards your monthly usage. Please contact support@zudello.com to confirm how creating documents will affect your billing. 

- Generating PDF for system generated document 
	- Generate PDF copies of system generated documents. PDFs will display all information from standard fields shown on the document within Zudello. 
	- For an additional charge, you can customise the standard generated PDF template to suit your business's branding.

- Duplicating documents
	- Duplicate a document with the click of a button.
	- The duplicated document will be opened in a new browser tab, and created in an editable status.
	- The duplicate can then be edited and submitted for approval and/or processing.
> All document values will be duplicated, including **Is Approved** flags and other hidden values

- Bulk actions
	- Bulk actions allow you to assign users to documents, change document statuses, or download original copies for multiple documents at once. 

- Related documents
	- Ensure visibility of the full procurement flow by creating relationships between documents. 
	- Any two documents can be related via the **Related Documents** tab. The relationship will then be visible on both documents.
	- When documents are matched for allocation purposes (e.g. allocating a purchase order to an invoice) the two documents will be related automatically.
	  
- File attachments on documents
	- Upload any related or supporting documents via the Related Attachments tab. Related attachments will then be visible to all other users (with the appropriate permissions).
	- Supported file types include csv, xls, pdf, jpg, png, and doc
	  
- Chat function
	- Zudello's chat function allows you to communicate and collaborate with other team members within documents. 
	- Tag other users within your message and they will receive a notification with a link directly to the document. 
	  
- Audit history
	- Zudello's audit history provides a comprehensive and granular history of every change made to a document, including:
		- Who made the change
		- When they made the change
		- The field/s affected
		- The original and updated values
	- Audit histories can not be edited or deleted, and can be downloaded as a PDF where required

- Approval history
	- A detailed approval history document (PDF) can be downloaded for any document that has undergone approval, regardless of the approval outcome. 
	- Approval history contains granular information for each approval step, including:
		- Name of the milestone and approval step
		- Timestamp of when the document was sent for approval
		- Name of the assigned approver
		- Approver's response
		- Timestamp of the response
		- Reason (for forced, changed, skipped or escalated approval)

- Emailing/rejecting documents including attachment
	- Easily send any rejected invoices back to the supplier by clicking the **Reject** button
	- An email window will open, with the supplier's email pre-filled. Enter your message and subject, and choose whether to attach the original invoice or not. 
	- ***The invoice will be sent from the relevant submodules default inbox.*** is this right??

# Document coding tools

- Calculations/validations as requested by the customer (from the available list)
	- Save time and ensure accuracy by turning on document validations and calculations. 
	- Calculations will calculate line and document total and tax amounts, while validations will ensure they conform to specific rules.  
	- Any valid combination of calculations/validations can be enabled (though some may conflict)
> Validations and calculations must be chosen from the existing list. Changes to the logic of validations and calculations, or the options available, may occur from time to time. 

- Supplier and item defaults
	- Teach Zudello how to code your documents with supplier and item defaults
	- Supplier defaults will be automatically applied when a supplier is matched to a document
	- Item defaults will be automatically applied when an item is selected on a document line, and will take precedence over supplier defaults
	- Defaults can be set to ask for confirmation, autofill when empty, or force replace existing values
	- Supplier and item defaults may be able to be fetched from your ERP (check your Solution Design for details)

- Item alternatives
	- Never change an item code twice again
	- Item alternatives allow you to teach Zudello to automatically switch out your suppliers' item codes for your internal item codes, ensuring easy matching between outgoing and incoming documents (e.g. POs and Invoices)
	- Item alternatives can be viewed and managed within each item card

- Supplier alternatives
	- Supplier alternatives let you teach Zudello to match invoices to the correct supplier, even when the name and other details don't match your record. 
	- This allows you to instantly match documents to the correct supplier, regardless of what name they use on their invoice. 
	- Supplier alternatives can be viewed and managed within each supplier item card

- ABN validation
	- Zudello's ABN validation offers live validation with the Australian Business Register's ABN Lookup, ensuring you are dealing only with valid suppliers. 
	- ABN validation will check the name of the supplier and their GST status.

- Bank account validation
	- Stop fraud at the first step with Zudello's bank account validation. 
	- When invoices are received, Zudello will automatically check the bank account details (BSB and Account Number) on the invoice with the account details saved against the vendor (where both details are available). If there is mismatch, a warning will be displayed so users can review and amend as required. 

# Data management tools
- [[Importing]]
	- Create and update data records in bulk by uploading a 
- Exporting
	- Get important data out of Zudello with exports
	- Customise your exports to contain exactly the fields you need, choose the date range, and filter by document status
	- Exports are generated as .csv files to give you maximum flexibility once you have downloaded them
- Language placeholders
	- Rename Zudello's standard fields to match your business's terminology, ensuring consistency and clarity across systems

# User functions
- Azure/Entra SSO, including user provisioning
	- Allow users to login via Entra AD single sign-on (SSO)
	- Entra can also be used for user provisioning to ensure your user access policies are consistent across systems
- User groups
	- Configure unlimited user groups to ensure your Zudello environment is in line with your business's security policies
	- User groups can be created, edited, and managed by organisation administrators
- Data permissions (unlimited, managed by customer)
	- Control who sees what with granular data permissions
	- Custom data permissions can be configured for each user group, or multiple user groups can be given the same data permissions

- Individual user notification settings
	- Users are able to configure their own notification settings, controlling which events they receive email notifications for

- Delegation including delegation of duties
	- When out of office, users can delegate their approvals (and optionally of their duties) to another user. 
	- This ensures approval flows can continue to function without the need to update DOAs
	- Each user can manage their own delegation, and organisation administrators can manager all users' delegation
- User default settings
	- User default settings will automatically apply certain coding when documents are uploaded by a user
	- User default settings can be managed by each individual user, or by organisation administrators
- 

# Support
- Australian-based support for the life of your plan with Zudello
	- (Brisbane business hours 9am - 5:30pm, no guaranteed response times, resolution times, or SLAs)