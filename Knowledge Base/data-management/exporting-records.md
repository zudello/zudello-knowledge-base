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

4. Click **Build export template**
5. Enter a template name
6. Choose your export type:
    1. Click **Download all** to export everything
    2. Click **Download selected** to export specific items
7. If downloading selected items:
    1. Select from the **Modules** drop-down
    2. Select from the **Submodules** drop-down
8. To add filters 
	1. Click **Add**
	2. Select from the **Select field** drop-down
	3. Select from the **Operator** drop-down
	4. Enter the value to filter on
	5. Repeat steps 1-4 for any additional filters
9. Click **Save**

### Creating a CSV export

10. Click **Build export template**
11. Enter a template name
12. Select from the **Modules** drop-down
13. Select  from the **Submodules** drop-down
14. Add your desired fields:
    1. Click **Add**
    2. Search or scroll to find fields
    3. Select the checkbox next to each field you want to include
15. To add filters 
	1. Click **Add**
	2. Select from the **Select field** drop-down
	3. Select from the **Operator** drop-down
	4. Enter the value to filter on
	5. Repeat steps 1-4 for any additional filters
16. Click **Save**

### Editing a template

17. Find the template in your templates list
18. Click **Edit template**
19. Make your desired changes
20. Click **Save**

## Exporting data

### Running an export

21. Find the template in your templates list
22. Click the play icon
23. Adjust any filters if needed
24. Click **Start**
25. Wait for the "Export queued" message

### Accessing export results

26. Click the refresh icon to update the list of ready exports
27. Monitor the export status
28. Once completed:
    - Click the download icon to download the export file
    - Click **Delete export** to delete the export file

## Need help?

Contact your organisation administrator or Zudello support for assistance with exports and data management.
