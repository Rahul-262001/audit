# Audit

# The Step-by-Step Guide to Unveiling the Creator
## Step 1: Confirm Cloud Audit Logs Activation
Verify that Cloud Audit Logs are active for your Google Cloud project. While typically enabled by default, a quick inspection of your project’s settings in Cloud Console under IAM & Admin > Audit Logs is advisable.

## Step 2: Access Audit Logs in BigQuery
With audit logs enabled, navigate to them in BigQuery. They reside within the special dataset _AUDIT_LOGS_ or the more recent cloudaudit_googleapis_com_data_access, requiring appropriate permissions to access.

## Step 3: Formulate and Execute the Query
Craft a query targeting the tables.insert call concerning your view’s inception. Here’s a template:

``` sql
SELECT
  protopayload_auditlog.authenticationInfo.principalEmail as creator,
  protopayload_auditlog.serviceData.tableInsertRequest.resource.tableId as viewName,
  TIMESTAMP_TRUNC(protopayload_auditlog.authenticationInfo.startTime, SECOND) as creationTime
FROM
  `projectId.cloudaudit_googleapis_com_data_access_*`
WHERE
  protopayload_auditlog.serviceData.tableInsertRequest.resource.tableId = 'yourViewName'
  AND protopayload_auditlog.methodName = 'google.cloud.bigquery.v2.TableService.Insert'
ORDER BY
  creationTime DESC
LIMIT 1;
```

Replace projectId and yourViewName suitably. This query filters the audit logs for your specific view’s tables.insert call, divulging the creator’s email, view name, and creation moment.

## Step 4: Delve into Query Outcomes
The query's output reveals the creator’s email, tied to the Google or service account executing the tables.insert call. This uncovers the individual or entity behind the view.
