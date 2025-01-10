# Dimension data

Dimensions are the values you code against transactions and transaction lines within Zudello. Common examples include accounts, departments, and tax rates. 

Keeping your dimension data up-to-date ensures accuracy and efficiency when processing documents. This guide explains how to view and manage dimension data effectively. 

### Best practices

To maintain data integrity across your systems:

- Manage dimension data within your ERP and let changes sync to Zudello
- Review dimension data regularly to ensure accuracy and remove unnecessary values
- Where possible, inactivate dimension data rather than deleting it to maintain accurate historical transactions
- Use consistent naming conventions when creating new dimension records

## Viewing dimensions

To access dimension data:

1. Click the company menu at the top right of your screen
2. Click **Settings**
3. Scroll down to the team data section in the left sidebar
4. Click the dimension you want to view

### Required permissions

To view dimension data, you will need the following permissions:

- Dimensions View
- Dimensions Visible
- For each dimension, you will then need:
	- Dimensions [DIMENSION NAME] View
	- Dimensions [DIMENSION NAME] Visible

### Understanding dimension statuses

Dimensions are grouped into the following standard statuses:

- **Active** 
	- These records appear in dimension drop-downs on transactions and transaction lines
- **Inactive**
	- These records won't appear in drop-downs and can't be selected for transactions or lines

## Managing dimension data

Dimension data automatically syncs from your ERP system as part of your integration. This integration:

- Eliminates the need to manage data in two systems
- Maintains consistency across both systems
- Updates regularly to ensure accuracy

As standard, Zudello fetches dimension data from your ERP daily at midnight UTC. 

Dimension data management should be handled within the ERP. All updates will flow through to Zudello at the time of the next sync. If you need to trigger a fetch urgently, please contact Zudello support for assistance. 

Some dimension fields may not exist in your ERP or may not be available via the integration. To manage dimension records within Zudello:

1. Use the search or filtering options to find the dimension you need
2. Click a dimension record to open it
3. Make your changes
4. Click **Save**

To edit dimensions within Zudello, you will need the following permissions:

- Dimensions View
- Dimensions Visible
- For each dimension, you will then need:
	- Dimensions [DIMENSION NAME] View
	- Dimensions [DIMENSION NAME] Visible
	- Dimensions [DIMENSION NAME] Update

## Need help?

Contact your organisation administrator or Zudello support for assistance with dimensions and data management.