# User groups in Zudello

Controlling user access and permissions is crucial for maintaining security in your organisation. This guide explains how user groups work in Zudello and how to manage them effectively.

## Understanding user groups

User groups control what users can see, do, and approve within Zudello. User groups can be granted access to any number of permissions within Zudello. When a user is assigned to a user group, they inherit all of the user groups permissions. 

User groups are classified into the following types:

- Access 
	- Access groups control what actions users can perform
	- Access groups should be configured with permissions that will be passed on to user assigned to the group
- Visibility 
	- Visibility groups are used in conjunction with data permissions to determine what information users can see
	- Visibility user groups should not have any permissions assigned
	- For more information on data permissions, see [data-permissions](data-permissions.md)
- Approval 
	- Approval groups are used in conjunction with approval automations to route documents to the correct approver
	- Approval user groups should not have any permissions
- Legacy
	- Legacy groups do not have a specific type and may be used for any of the above categories
	- If you have legacy user groups that fit into one of the categories above, we suggest changing the user group type
	- New user groups should never be set up as legacy groups


## Best practice

- Place all access permissions within access user groups
- Keep all visibility settings within visibility user groups
- Use approval groups solely to help route approvals 
- Do not create any new legacy groups

## Viewing and editing user groups

### Accessing user groups

User groups are managed at the organisation level. To access user group information:

1. Click the company menu at the top right of your screen
2. Click your organisation name
3. Click **User groups**

### View permissions

The **Permissions** column shows the number of permissions applied to each user group. To view the specific permissions that apply to a group: 

1. Find the user group you want to inspect
2. Click the edit icon at the end of the row
3. In the user group modal that opens, you can:
   - Turn on 'Show selected only' at the top of the table to view only applied permissions
   - Expand each permission group to see individual permissions
   - Search for specific permissions using the search bar at the top right
   > When searching permissions, turn off 'Show selected only' to search all available permissions

### Edit permissions

To edit the permissions that apply to a group: 

1. Click the edit icon next to the user group
2. Select and deselect permissions as needed
3. Ensure you select all related permissions for full functionality
   > E.g. to allow users to update purchase invoices, you need to grant:
   > - Purchase invoice update permission
   > - Purchase invoice view permission
   > - Purchase invoice visible permission
4. Click **Update** to save your changes

If you're unsure about permission interactions, contact your organisation administrator or Zudello support.

### Configure delegation options

The **Can be delegated** option at the top of the user group modal controls whether permissions within that group apply to delegates when a user delegates their duties.

For more information about delegation, see our Managing delegation and default coding article.

### Creating a user group

As your business grows, you may need to add additional user groups. To create a new user group:

1. Click **Create**
2. Enter a name and description for the user group
3. Configure the user group type, permissions, and delegation options
4. Click **Create**

The user group will be created, and you can now begin to add users to the group.

### Deactivate a user group

From time to time you may need to deactivate certain user groups due to changes in your security policies. To deactivate a user group:

1. Click the edit icon next to the user group
2. Turn off 'Is active' at the top right
3. Click **Update**

The user group will be deactivated and its permissions will no longer apply to any group members.

## Managing group membership

The group membership page gives you an overview of the user groups within your organisation, and the users that are members of each group. To access the group membership page:

1. Click the company menu at the top right of your screen
2. Click your organisation name
3. Click **Group membership**
### View group members

The group membership page shows you which users belong to each user group.

- Click the arrow at the start of a row to expand a user group and see all members
- Use the search bar at the top right to find specific user groups
- To filter to a specific team, click **Select team** and select from the drop-down

### Add users to a group

To quickly add users to a user group:

1. Click the **+** icon at the end of the row
2. Click **Add**
3. Select users from the dropdown (you can search if needed)
4. Click **Done**
5. Click **Add Users** to complete the process
> Make sure to check whether you are adding users to one team or all teams in your organisation

### Remove users from a group

To quickly remove users from a user group:

1. Find the user group in the group membership list
3. Click the arrow at the start of a row to expand the group
4. Click the delete icon next to the user's name
> Make sure to check whether you are removing users from one team or all teams in your organisation

The changes to group membership save automatically.

## Need help?

Contact your organisation administrator or Zudello support if you need assistance with user group configuration.