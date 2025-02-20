# Dependencies

Dependencies help you create smart, contextual field relationships in Zudello. When configured, they automatically limit the options in one field based on what you select in another. This guide explains how to view and manage dependencies for your organisation.

## Best practices

- Review your business rules before setting up dependencies
- Consider the impact on all affected users before configuring dependencies
- Consider using your ERP to configure dependencies when available
- Keep dependencies simple and logical
- Test dependencies thoroughly after configuration

## Understanding dependencies

Dependencies create relationships between fields, such as:

- Limiting location options based on selected subsidiary
- Limiting item choices based on the matched supplier

Zudello applies dependencies automatically to documents. When you select a value in the controlling field, the dependent field only shows relevant options.

## Setting up dependencies

### Using ERP integration

If your ERP system manages field relationships, you can pull these through to Zudello:

1. Set up the rules in your ERP
2. Zudello pulls these rules when fetching dimensions
3. Dependencies are automatically saved in Zudello

This approach uses your ERP as the source of truth and eliminates duplicate maintenance.

### Manual configuration

Dependencies can be configured manually within Zudello. For the following steps we will use the example of setting up dependencies to limit the available locations based on the subsidiary selected. 

To set up a new dependency manually:

4. Click the company menu at the top right
5. Click **Settings**
6. Click the dependent dimension (e.g. location)
7. Find and open the specific dimension value you want to configure
8. Click the dependencies icon at the top right
9. Click **Add** 
10. Select the controlling resource (e.g. subsidiary) from the **Depends on** drop-down
11. Select the specific value to depend on from the **Resources** drop-down
12. Click **Save**

To remove a dependency:

13. Find and open the specific dimension value you want to configure
14. Click the dependencies icon at the top right
15. Click the delete icon next to the dependency you want to remove
16. Click **Save**

## Testing dependencies

To verify your configuration:

17. Open a document
18. Select a value in the controlling field
19. Check that the dependent field  drop-down shows only the expected options
20. Test multiple combinations to ensure all relationships work correctly

## Important notes

- Dependencies work alongside other filters like inactive value filtering
- If no dependencies exist, fields show all available options
- Dependencies apply globally to each team
- You cannot set different dependencies for different users on the same team

## Need help?

Contact your organisation administrator or Zudello support for assistance with dependency configuration.