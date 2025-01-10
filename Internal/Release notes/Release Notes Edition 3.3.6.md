###### Release Date: 5th November 2024  
###### Version: v3

Here's the latest summary of what’s new and improved in Zudello, as well as what was resolved in the latest release.

# New and improved

### Dependencies

Zudello's dependencies feature allows you to filter available options in one field based on the value chosen in another. 

We now support limiting the list of available suppliers based on the subsidiary or location chosen on a document. If a user chooses a subsidiary or location before selecting a supplier, we can limit the list of suppliers to only those suppliers that:
- are listed as being available for the selected subsidiary / location, or
- have no dependency data saved (i.e. are not subsidiary / location depdendent)

These dependencies will also take effect during enrichment, which is the process after document extraction where Zudello links the relevant company (supplier or customer), item, and dimension information. Once enrichment links a company, Zudello will now check the following:
- If there is a subsidiary / location set against the lines (from a keyword document coding rule or some other 'On upload' automation)
- If not, if there is either:
	- a default subsidiary / location set against the inbox the document was received by (emailed documents only), or
	- a default subsidiary / location set against the user who created or uploaded the document 
- If the above rules produce a single subsidiary / location, when linking a company we will filter to only those companies that are:
	- listed as dependent on the subsidiary / location, or
	- listed as having no dependencies on subsidiary / location
- If the above rules produce multiple subsidiaries / locations (i.e. there are different subsidiaries / locations on each line), we will not use the dependency checks

To check whether your team currently uses dependencies, please contact support@zudello.com
### Mileage expenses

Calculating and tracking mileage is simpler than ever with our new Mileage Expenses for reimbursement claims. 

Users can now create Mileage Expenses by entering the locations they've travelled to and from, and Zudello will calculate the route and distance between the two points. This distance can then be used in conjunction with preset mileage rates to quickly and easily determine the value of mileage reimbursement expenses. 

The new mileage expense form uses Google maps to determine the route and distance between points. Users can add multiple stops to ensure they track all required travel, without needing to process multiple mileage expenses for a single day of travel.

To learn more about enabling Mileage Expenses for your team, please contact support@zudello.com
### Validation tolerance on forms

Validations are used to ensure that values on documents are correct. Common validations check that the sum of line totals equals either document subtotal or total, that the total tax field is equal to the line tax amounts, and more.

We now support customisable tolerances on validations, to account for slight rounding discrepancies and other minor differences. The default tolerance applied to all document types on Zudello V3 is $0.0201, but this can be customised for each document type in your team. 

To adjust the validation tolerances on your forms, please reach out to support@zudello.com

# Resolutions

We are constantly working to refine Zudello functionality and ensure that any issues are addressed as soon as possible. As part of this release, we have made the following resolutions and improvements:

- We resolved an issue where Keyword Coding Rules were not correctly applied due to case sensitivity. All keyword lookup rules are now case insensitive.

- We have restricted which modules and submodules can be selected when converting a document. The following list details conversions that are NOT allowed (structure is Existing Submodule > Converted Submodule)
	- Expenses > Mileage
	 - Expenses > Claim
	 - All Modules (Expenses, Sales, Purchasing, Relationships) > Requests

 - We have improved exporting selections and filter behaviour when selecting module and submodule

 - We have resolved an issue with document URLs displaying incorrectly when a document was opened from the inbox. When you navigate from the inbox to a document, the URL will now refresh properly and display the URL of the document

- When users are making a configuration change to dataset fields, we now display a warning and await confirmation before clearing data to prevent accidental deletes. This is in in addition to the existing warning that displays when you change the dataset type. 

- Users can now view the associated Tax Solution on a Tax Rate form if the field is enabled. If you would like to discuss enabling this field please contact support@zudello.com
# Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.