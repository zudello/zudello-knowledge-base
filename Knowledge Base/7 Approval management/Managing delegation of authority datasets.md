#  Managing delegation of authority datasets

We know that conditions and people change, especially in dynamic growing companies. With Zudello, you can easily view and edit your delegation of authority (DOA) dataset to control approval routing and limits within your team. 

### Best practices

- Review your DOA settings regularly to ensure they reflect current approval requirements
- Double-check limit amounts when making changes
- Consider using user groups instead of individual users for easier maintenance
- Keep your approval routing structure as simple as possible while meeting your needs

## Accessing DOA datasets

1. Click the company menu
2. Click **Settings**
3. Scroll down the left menu and click **Datasets**
4. Look for the dataset with ‘DOA’ or ‘Delegation of Authority’ in the name  
> To confirm your DOA dataset name, contact your organisation administrator or Zudello support.

To view datasets, you will need the following permissions:
- Dataset Visible
- Dataset View
- Dataset List
- Dataset Row View

To edit datasets, you will also need the following permissions:
- Dataset Edit
- Dataset Row Create
- Dataset Row Update
- Dataset Row Delete

## Viewing DOA datasets

### Understanding DOA dataset Columns

DOA datasets contain several important columns that control how approvals are routed:
- Step name
	- Displays the name that will appear on each approval step when documents are sent for approval.
- User or User Group
	- Specifies which user or user group will receive approval requests for each row in the dataset.
- Limit
	- Defines the approval limit amount for each user or user group.
	- This limit can be checked against either the transaction total, or the sum of all matched lines. To check which option applies to your team, please contact your organisation administrator or Zudello support
- Dimension Names (e.g. Department, Account, Location)
	- Shows the dimension values that will be used to match transaction lines with the relevant DOA row/s
	- Any blank fields will be treated as wildcards, and will be considered a match for all transactions

### Search and filter options

To find specific entries quickly:
- Use the search bar for general searches
- Sort columns by clicking the column header
- Click the menu icon in any column header to access filtering options

## Making changes to your DOA dataset

### Editing existing entries

1. Click the Edit dataset rows button on the right 
2. Double-click into any field you want to modify
3. Enter the new values by:
	- Typing directly for free text fields
	- Selecting from dropdown menus for list-based fields
4. Click anywhere outside the field and the changes will be saved automatically

### Adding new entries

1. Click "Add Row" at the top left of the dataset
2. A new row will appear at the bottom of the dataset
3. Fill in the required information per the Editing existing entries instructions above

### Removing entries

1. Select the checkbox next to the row you want to remove
2. Click Remove selected at the top

### Next steps

After making changes to your DOA dataset, simply close out of the editor - your changes will be saved automatically. Test your new settings by creating a test document to ensure approvals are routing as expected.

## Need help? 

Contact your organisation administrator or Zudello support for assistance with your DOA configuration.