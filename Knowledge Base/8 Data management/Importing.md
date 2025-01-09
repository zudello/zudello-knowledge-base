# Importing data in Zudello

We know that managing data can be challenging. With Zudello's importing feature, you can efficiently create new records or update existing ones in bulk, giving you more control over your team's data.

## Best practices

- Review and clean your data before importing
- Ensure all referenced data exists in Zudello before importing
- Test imports with a small sample before processing large datasets
- Double-check field mappings before proceeding with the import
- Document any significant data transformations

## Required permissions

To use the importing function, you will need the following permissions:

- System Import View
- System Import Create
- System Import Update
- System Import Delete (optional for deleting previous imports)
- And for each submodule you want to import to:
	- Module Submodule Import
	- Module Submodule Create
	- Module Submodule Update

Contact your organisation administrator to check or modify your permissions.

## File requirements

Your import file must meet these criteria:

- Use CSV or TXT format (Excel files must be converted to CSV)
- Include a header row to define columns
- Use unique column headers for accurate field mapping
- Format dates as YYYY-MM-DD

## Importing process

### Create and map your import

1. Click the company name in the top right of your screen
2. Click **Settings** 
3. Click **Imports**
4. Click **Create**
5. Select from the **Module** drop-down
6. Select from the **Submodule** drop-down
7. Optionally, select from the **Form** and/or **Status** drop-downs to apply one form and/or status to all imported records
8. Click **Continue**
9. Upload your file by either:
    - Dragging and dropping onto the screen
    - Clicking **Click here to upload**
10. Map your columns to Zudello fields
11. Click **Continue**

### Review import results

Monitor your import's status in the Imports tab. Import statuses are:

- Queued
	- Import awaiting processing
- Successful
	- All records imported correctly
- Failed
	- Import unsuccessful, no records imported
	- For failed imports:
		1. Click the icon next to the status
		2. Review the detailed error explanations
		3. Correct the issues in your import file
		4. Create a new import and try again

## General rules and restrictions

- Not all columns need to be mapped
- When referencing Zudello data (e.g. referencing default Tax Rate when importing Items), all referenced values must already exist within Zudello (e.g. the import tool will NOT create a new Tax Rate when importing Items if the referenced Tax rate does not exist)
- When referencing Zudello data, use any of the following fields:
    - **UUID** 
    - **Code**
    - **External ID**
> You cannot reference other records using their **Name**
- Where records already exist, importing can be used to update rather than create records
	- Provide the UUID of each record to ensure accurate updates

## Importing transactions

Transaction imports allow you to:

- Import single or multiple transactions and their lines
- Select the appropriate module and submodule
- Optionally enable auto-generation of document numbers

Simply follow the same importing process as detailed above.

### Creating multi-line transactions

When importing multi-line transactions, lines can be grouped using either:

- A separate column for a unique transaction number (preferred method)
- Unique supplier and document number combination

### Updating existing transactions

When updating transactions:

- Include a transaction UUID and line UUID for each row
- Leave blank any fields you don't want to change
- Ensure UUIDs match existing records exactly
## Supported record types for importing

Record types currently available for use with the Zudello importing feature are:

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
    - Expense Categories
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
    - Amortisation Schedule
    - Fixed Assets
    - Mileage Rates
    - Item Categories
    - Item Groups
    - Payment Methods
    - Payment Types
    - Supplier Categories
    - Supplier Groups
    - Countries
    - Time zones
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

## Need help?

Contact your organisation administrator or Zudello support for assistance with importing.