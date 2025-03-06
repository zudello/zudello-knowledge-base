# Microsoft Entra ID (Azure AD) - Single sign-on (SSO)

Set up Microsoft Entra ID (formerly Azure AD) authentication to enable secure single sign-on for your Zudello implementation. This guide explains how to configure the required application settings and permissions in Entra ID.

## Best practices

To ensure smooth authentication setup:

- Generate client secrets with appropriate expiration dates
- Grant all required permissions before implementation
- Save authentication keys in a secure location
- Review permissions regularly to maintain security
- Test authentication after making any changes

## Creating Entra ID authentication credentials

To set up Entra ID SSO for your Zudello team, you will first need to:

1. Register a new client
2. Add a client secret
3. Configure token settings
4. API permissions

### Registering a new client

1. Open the [App registration menus create dialog](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false) 
2. Enter **Zudello** as the name of the application a name
3. Select who should be able to login (Single-Tenant, Multi-Tenant, Personal Accounts). This setting will impact how you configure the provider later on in Zudello.
4. Select **Web** under **Redirect URI** and paste the following Zudello callback URL 
	https://auth.1.global.zudello.io/ui/login/login/externalidp/callback
5. Save the **Application (client) ID** and the **Directory (tenant) ID** from the detail page in a secure location
6. Click **Register**

*Example registration page*

![](../images/Pasted%20image%2020250113093632.png)

*Example Application (client) ID and Directory (tenant) ID*

![](../images/Pasted%20image%2020250113093644.png)
### Adding a client secret

To generate a new client secret to authenticate your user:

7. Click **Client credentials** on the detail page of the application, or **Certificates & secrets** in the side menu
8. Click **New client secret** 
9. Enter a clear description and a suitable expiry date
> Record the expiry date in your organisation's calendar with suitable notice to avoid any future disruptions when refreshing tokens
10. Click **Add**
11. Copy the secret value
> Ensure you copy the secret now as you will not be able to see it again.


![](../images/Pasted%20image%2020250113093653.png)

### Configuring token settings

Configure the token to return required user information:

12. Click **Token configuration** in the side menu
13. Click **Add optional claim**
14. Add the following claims to the id token:
    - email
    - family_name
    - given_name
    - preferred_username

![](../images/Pasted%20image%2020250113093710.png)

### Setting up API permissions

Configure the correct API permissions to enable all required functionality:

15. Click **API permissions** in the side menu
16. Verify the following Microsoft Graph permissions are included:
    - email
    - profile
    - User.Read
    - openid

![](../images/Pasted%20image%2020250113093741.png)

17. Click **Grant consent** to apply the permissions

![](../images/Pasted%20image%2020250113093755.png)

## Completing implementation

Once you have completed the above steps, please securely provide these authentication keys to Zudello:

- Application (Client) ID
- Directory (tenant) ID
- Client Secret value

To ensure your information is kept confidential, use a secure password sharing tool like 1Password or LastPass. If you do not have access to any such tool, please send Client IDs and Client Secret values in separate messages. 
## Need help?

Contact your organisation administrator or Zudello support for assistance with Azure AD authentication setup.