# User groups in Zudello

We know that controlling access and permissions is crucial for maintaining security in your organisation. This guide explains how user groups work in Zudello and how to manage them effectively.

## Understanding user groups

User groups control what users can see, do, and approve within Zudello. User groups can be granted access to any number of permissions within Zudello. When a user is assigned to a user group, they inherit all of the user groups permissions. 

TUser groups broadly fall into one of three categories:

- Access 
	- Access groups control what actions users can perform
	- Access groups should be configured with permissions that will be passed on to user assigned to the group
- Visibility 
	- Visibility groups are used in conjunction with data permissions to determine what information users can see
	- Visibility user groups should not have any permissions assigned
	- For more information on data permissions, see [[Understanding data permissions]]
- Approval 
	- Approval groups are used in conjunction with approval automations to route documents to the correct approver
	- Approval user groups should not have any permissions
- Legacy
	- Legacy user groups



Best practice is to keep these group types separate and distinct:
- Place all access permissions within access user groups
- Keep all visibility settings within visibility user groups
- Use approval groups solely to help route approvals 

## Viewing and editing user groups

### View permissions

1. Find the user group you want to inspect
2. Click the pencil icon at the end of the row
3. In the user group modal that opens, you can:
   - Toggle 'Show selected only' at the top of the table to view only applied permissions
   - Expand each permission group to see individual permissions
   - Search for specific permissions using the search bar at the top right
   > When searching permissions, turn off 'Show selected only' to search all available permissions

### Edit permissions

1. Open the user group modal using the pencil icon
2. Select or deselect permissions as needed
3. Ensure you select all related permissions for full functionality
   > For example, to allow users to update purchase invoices, you need to grant:
   > - Purchase invoice update permission
   > - Purchase invoice view permission
   > - Purchase invoice visible permission

4. Click **Update** to save your changes

If you're unsure about permission interactions, contact your organisation administrator or Zudello support.

## Managing group status

### Deactivate a user group

1. Click the pencil icon next to the user group
2. Turn off 'Is active' at the top right
3. Click **Update**

The user group will be deactivated and its permissions will no longer apply to any users.

### Configure delegation options

The 'Can be delegated' option at the top of the user group modal controls whether permissions within that group apply to delegates when a user delegates their duties.

For more information about delegation, see our Managing delegation and default coding article.

## Managing group membership

### View group members

The group membership tab shows you which users belong to each user group.

1. Click a user group to expand it and see all members
2. Use the search bar at the top right to find specific user groups
3. Filter by team using the team selector

To view membership across all teams:
1. Click the currently selected team
2. This deselects the team and shows all teams' memberships

### Add users to a group

1. Click the Add User icon next to the user group
2. Click **Add**
3. Select users from the dropdown (you can search if needed)
4. Click **Done**
5. Click **Add Users** to complete the process

### Remove users from a group

1. Find the user in the group membership list
2. Click the delete icon next to their name

Changes to group membership save automatically.

## Need help?

Contact your organisation administrator or Zudello support if you need assistance with user group configuration.