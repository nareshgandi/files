### Objective: Implement a database security model for the Pghyd organization to manage employee data while ensuring data privacy and compliance.

#### Key Requirements:
###### User Roles and Permissions:

1. **pghyd_viewer**: Limited access to specific columns (e.g., cannot see salary or phone number).
2. **pghyd_core**: Full access to all data and operations.
3. **pwi_core**: Manage PWI-specific records with full access.
4. **pwi_regular**: Read-only access to PWI records, with no modification rights.

#### Data Privacy and Security:

1. Implement Row-Level Security (RLS) to restrict data access based on roles.
2. Prevent certain roles from deleting records to maintain data integrity.

#### Column-Level Security:

1. Protect sensitive information (salary, phone number) using encryption and restrict access to specific roles.

#### Auditing and Compliance with pgAudit:

Ensure that all actions on employee records comply with data governance policies, with tracking of access for audits.
