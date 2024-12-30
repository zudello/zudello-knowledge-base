
Zudello's importing functionality can be used to bulk update or create records within Zudello. For a full list of records that are available for use with the importing feature, please see the 'Support Record Types' section below.

#### Permissions

In order to use the importing function, you will need the appropriate permissions. To check or amend your permissions, please speak to your Organisation Administrator.

#### File requirements

- Import files must be in .csv or .txt format. Excel files (.xlsx or .xls), or other spreadsheet files, will need to be converted to .csv format before using the import feature.
- Import files must have a header row. If there is no header row, the first line of data will be treated as a header row and will be excluded from the import. 
- Column headers must be unique in order to be mapped into different fields within Zudello. Any columns with the same header will be mapped into the same field.
- **Date Issued**, **Date Due** and **Date Posted** need to be imported using the following format - **YYYY-MM-DD**

#### The importing process

##### Create and map the import

- Navigate to **Settings** > **Imports**
- Click **Create**
- Select the Module and Submodule you want to import into.
> You cannot run a single import for records in different submodules 
- Optionally, select the relevant Form and Status you want to apply to all imported records.
> This option will set the same Form and Status on all imported records. To import records with differing Form and/or Status types, provide the Form and Status within the import file itself.
- Select **Continue** 
- The upload screen will now display. Upload your file by either:
	- drag and dropping the file on to the screen, or
	- clicking **Click here to upload** and selecting the file to upload
- You will be presented with a preview of the uploaded file, and you can then map each column of the file to the relevant Zudello field. The list of fields is searchable, and will be limited to those in the Module and Submodule you are importing into.
- Once you have mapped all relevant columns, click **Continue**
- The import will then be queued for processing

##### Review your import

A list of all team imports are displayed in the Imports tab. The status next to your import will change as your import moves through the process.   
Current import statuses are:
- Queued
	- The Import has been queued for processing. This can take some time for large import files.
- Successful
	- All records have been successfully imported. No further steps are required from the user.
- Failed
	- The Import has failed, and no records have been imported
    - You can view a detailed breakdown of the errors by clicking the icon next to the status name
	    - Zudello provides a detailed explanation of the error, including the field the user was trying to import, the value provided in the file, and the Row Number the error applies to. Row numbers are generated exclusive of the Header Row.
    - Resolve the error/s in the file you are importing, create a new import, and try again
    

#### General rules and restrictions

- When mapping columns, not all columns need to be mapped
- When referencing other Zudello data (e.g. referencing default Tax Rate when importing Items) all referenced values must already exist within Zudello (e.g. the import tool will NOT create a new Tax Rate when importing Items if the referenced Tax rate does not exist)
- When referencing other Zudello data, use any of the the following fields:
	- **UUID** - an auto-generated, unique system ID for all Zudello records
	- **Code** - populated by the user or the integration, NOT currently enforced to be unique
	- **External ID** - the unique ID of the record in your external system, usually populated when the record is fetched from your integration. Not currently enforced to be unique within Zudello, but usually required to be unique within your external integration
> You cannot reference other records using their **Name**
- Where records already exist within Zudello, importing can be used to update rather than create the records. When updating, provide the UUID of each record to ensure consistent and accurate updates

#### Importing transactions

- Transactions can be imported in bulk, allowing you to import a single or multiple transactions along with their lines in a single import file
- Importing can be used to create new transactions, or updating existing transactions
- Select the Module & Submodule you are importing into. You cannot run a single import across multiple submodules (e.g. import Invoices and Purchase Orders at the same time)
> The available import fields and their names may change based on the Submodule selected
- We do not currently support importing to the following Submodules
	- Claims, Mileage, Refunds (Expenses module)
	- Statements, Payments, Refunds (Purchasing module)
	- Payments, Refunds (Sales module)
	- Backorders, Shipments (Inventory Module)
- Optionally, select a Document Type and Status to be applied to all Transactions that are being imported. Alternatively, Status and Document Type information can be provided per transaction in the upload file 
- Optionally, you can opt to Auto-generate Document Numbers
	- This requires the selected Document Type to have a Computed Fields rule configured. Please contact Zudello Support to check that this has been applied
	- If a rule is configured, we will automatically generate the Document Number
	- If no rule is configured, the import will be successful but we will not generate the Document Number
###### Importing bulk transactions

- To allow the system to understand which rows in the import file should be grouped into a single transaction, use a field called **Transaction Number**
- Zudello will group all rows that have the same **Transaction Number** into a single transaction
> For multi-line transactions, we will take the Transaction header information from the first row for each Transaction Number. You do not need to repeat Header information for subsequent lines of the same transaction.
- Alternatively, if no Transaction Number is provided we will group each unique Supplier and Document Number combination into a single Transaction. In this case, the Supplier and Document Number should be repeated for each applicable row.

###### Updating existing transactions
- To execute an update, both the Transaction UUID and Transaction Line UUID need to be present for every row of the file. You cannot use the transaction or line external ID to update transactions or their Lines
- You do not need to provide a Transaction Number for updates
- Any fields that are left blank (empty cells) will be ignored in the import and remain unchanged in Zudello

#### Supported record types

The following list details all record types that are currently available for use with the Zudello importing feature.  
- Relationships
	- Suppliers
	- Customers
	- Employees
- Dimensions
	- Accounts
	- Account Groups
	- Accounting Periods
	- Team Addresses
	- Cost Centres
	- Cost Types
	- Departments
	- Subsidiaries
	- Location
	- Warehouses
	- Zones
	- Expense Catgeories
	- Tax Rates
	- Tax Solutions
	- Projects
	- Project Groups
	- Project Tasks
	- Project Types
	- Units of Measure
	- Batches
	- Bins
	- Currencies
	- Customer Categories
	- Customer Groups
	- Amortisation Schedule Fixed Assets
	- Mileage Rates
	- Item Categories
	- Item Groups
	- Payment Methods
	- Payment Types
	- Supplier Categories 
	- Supplier Groups
	- Countries
	- Timezones
- Purchasing
	- Quotes
	- Requisitions
	- Orders
	- Invoices
	- Returns
	- Credits
	- Payments
- Sales
	- Quotes
	- Requisitions
	- Orders
	- Invoices
	- Returns
	- Credits
	- Payments
- Inventory
	- Catalogue (including Item Alternatives)
	- Receipts
- Expenses and Travel
	- Expenses
	- Payments

#### Any questions?
If you have any questions about importing, or are unsure about any part of the process, please reach out to support@zudello.com