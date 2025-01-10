# Data permissions

Ensuring users can see only the information they need is crucial for your organisation's security. This guide explains how to manage data permissions to ensure users have the right level of visibility across different teams.

## Best practices

- Review data permissions regularly to ensure they align with your security requirements
- Document any significant changes to data permission settings
- Keep data permission structures as simple as possible while meeting your needs

## Understanding data permissions

Data permissions work with user groups to control what users can see within Zudello. 

Each data permission is given access to certain resources within Zudello. Data permissions are then assigned to one or more user groups. Users within those user groups will then inherit the data permissions, giving them access to all resources selected under the data permission.
Some important things to remember are:

- Permissions are controlled at the team level
- Users can have different data permissions across different teams
- Data permissions are applied to one or more user groups
- All users who belong to a user group inherit the data permissions applied to that user group

## Viewing and editing permissions

To access data permissions:

1. Click the company menu at the top right of your screen
2. Click **Settings**
3. Click **Data permissions** in the left sidebar

### Viewing existing permissions

The data permissions table shows all permissions and their associated user groups. To view details for a specific permission:

1. Find the permission in the data permissions table
2. Click the edit icon next to the permission
3. Review the permission details in the modal:
    - Permission name
    - Assigned user groups
    - Resource access settings

### Adding resource permissions

To add access to a new resource:

1. Open a data permissions
2. Click **Add permission**
3. Select the resource from the drop-down menu
4. Choose the permission type:
    - **All**: Grants access to all records within the resource
    - **Own**: Limits access to records assigned to the user
    - **Related**: Controls access based on relationships to other resources

### Setting up related permissions

When using related permissions:

1. Select **Related** as the permission type
2. Click the **If has access to** drop-down
3. Choose the related resource
4. Select the appropriate access level for the related resource

For example, to allow users to see message threads only for transactions they're assigned to:

1. Click **Give access to** 
2. Select **Message Threads** 
3. Click **Select option** (this will be prefilled to **All** by default)
4. Select **Related**
5. Click **If has access to**
6. Select **Transaction** 
7. Click **Select option**
8. Select **Own**

### Removing resource permissions

To remove access to a resource:

1. Find the resource in the permissions list
2. Click the delete icon next to the resource
3. Click **Save** to apply the changes

## Creating new data permissions

1. Click **Create**
2. Enter a name for the new permission
3. Select the user groups this permission applies to
4. Add relevant resource permissions following the steps above
5. Click **Save**

## Deleting data permissions

1. Find the permission in the data permissions table
2. Click the delete icon next to the permission
3. Click **Yes**

## Need help?

Contact your organisation administrator or Zudello support for assistance with data permissions configuration.