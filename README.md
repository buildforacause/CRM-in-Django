# CRM-in-Django
This webapp in django demonstrates a CRM (Customer relationship management) styled using TailwindCSS

# What is CRM?
Customer relationship management (CRM) is a technology for managing all your company’s relationships and interactions with customers and potential customers. The goal is simple: Improve business relationships. A CRM system helps companies stay connected to customers, streamline processes, and improve profitability.

You can read more [here.](https://www.salesforce.com/in/crm/what-is-crm/)

# About Webapp
This webapp is created in Django and styled in TailwindCSS.
This is not yet responsive for mobile view but will try to improve it soon.

This app has two views:
1] Organizor: The organization which manages all the agents and leads under them. They have all the CRUD permissions.
2] Agents: The agent who manages all the leads assigned under them. They have a view only permission from which they can view the status of the leads under them.

There are different categories under which leads may segment into.
For now there are 3 categories: Contacted, Converted, Unconverted.
The newly created leads will have New Category as default. However, the organization have the permission to update it.
