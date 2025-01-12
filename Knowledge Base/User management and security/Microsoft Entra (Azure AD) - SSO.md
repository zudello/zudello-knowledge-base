# Microsoft Entra ID (Azure AD) - Single sign-on (SSO)

Set up Microsoft Entra ID (Azure AD) authentication to enable secure single sign-on for your Zudello implementation. This guide explains how to configure the required application settings and permissions in Entra ID.

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

- Browse to the [App registration menus create dialog](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false) to create a new app

- Give the application a name and choose who should be able to login (Single-Tenant, Multi-Tenant, Personal Accounts, etc.) This setting will have an impact on how to configure the provider later on in Zudello.

- Select "Web" in the redirect URI field and paste the following Zudello callback URL:
  https://auth.1.global.zudello.io/ui/login/login/externalidp/callback

- Save the **Application (client) ID** and the **Directory (tenant) ID** from the detail page in a secure location

- Click **Register**

Example registration page

![[Pasted image 20250113091642.png]]

Example Application (client) ID and Directory (tenant) ID

![[Pasted image 20250113091727.png]]
### Adding a client secret

To generate a new client secret to authenticate your user:

1. Click **Client credentials** on the detail page of the application, or **Certificates & secrets** in the side menu
2. Click **New client secret** 
3. Enter a clear description and an expiry date
4. Click **Add**
5. Copy the secret value
> Ensure you copy the secret now as you will not be able to see it again 

### Configuring token settings

Configure the token to return required user information:

1. Click **Token configuration** in the side menu
2. Click **Add optional claim**
3. Add the following claims to the id token:
    - email
    - family_name
    - given_name
    - preferred_username

### Setting up API permissions

Configure the correct API permissions to enable all required functionality:

1. Click **API permissions** in the side menu
2. Verify the following Microsoft Graph permissions are included:
    - email
    - profile
    - User.Read
    - openid
3. Click **Grant consent** to apply the permissions

## Completing implementation

Provide these authentication keys to Zudello:

- Application (Client) ID
- Directory (tenant) ID
- Client Secret value

## Need help?

Contact your organisation administrator or Zudello support for assistance with Azure AD authentication setup.