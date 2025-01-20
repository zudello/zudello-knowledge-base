# Exporting data in Zudello

Getting your data out of Zudello in the right format is crucial for your analysis and reporting. This guide explains how to create and manage custom exports for your transaction, relationship, and dimension data.

## Best practices

To ensure efficient and effective use of exports:

- Only add necessary fields to keep exports fast and manageable
- Use filters when exporting from submodules with a large number of records
- Avoid running the same export repeatedly in quick succession
- Use clear, descriptive names when creating export templates

## Required permissions

To access and run exports, you will need the following permissions:

- System Export View
- System Export Create
- System Export Update
- Export Template List
- Export Template View
- Export Template Visible
- Export Template Edit (optional if required to create and update export templates)
- For each submodule you need to export, you will need:
	- Module Submodule Export

## Accessing exports

1. Click the company menu at the top right of your screen
2. Click **Settings**
3. Click **Exports**

In the exports section, you'll find:

- Templates
	- Your team's saved export templates
- Ready exports 
	- Previously generated export files

To view only the export files that you have generated, turn on **Show mine only**.

## Managing export templates

### Creating an export for original files

1. Click **Build export template**
2. Enter a template name
3. Choose your export type:
    1. Click **Download all** to export everything
    2. Click **Download selected** to export specific items
4. If downloading selected items:
    1. Select from the **Modules** drop-down
    2. Select from the **Submodules** drop-down
5. To add filters 
	1. Click **Add**
	2. Select from the **Select field** drop-down
	3. Select from the **Operator** drop-down
	4. Enter the value to filter on
	5. Repeat steps 1-4 for any additional filters
6. Click **Save**

### Creating a CSV export

1. Click **Build export template**
2. Enter a template name
3. Select from the **Modules** drop-down
4. Select  from the **Submodules** drop-down
5. Add your desired fields:
    1. Click **Add**
    2. Search or scroll to find fields
    3. Select the checkbox next to each field you want to include
6. To add filters 
	1. Click **Add**
	2. Select from the **Select field** drop-down
	3. Select from the **Operator** drop-down
	4. Enter the value to filter on
	5. Repeat steps 1-4 for any additional filters
6. Click **Save**

### Editing a template

1. Find the template in your templates list
2. Click **Edit template**
3. Make your desired changes
4. Click **Save**

## Exporting data

### Running an export

1. Find the template in your templates list
2. Click the play icon
3. Adjust any filters if needed
4. Click **Start**
5. Wait for the "Export queued" message

### Accessing export results

1. Click the refresh icon to update the list of ready exports
2. Monitor the export status
3. Once completed:
    - Click the download icon to download the export file
    - Click **Delete export** to delete the export file

## Need help?

Contact your organisation administrator or Zudello support for assistance with exports and data management.
