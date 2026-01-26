# Create Workspace-level audit logs

Create Workspace-level audit logs. Audit logs can only be created by the Workspace owner on Enterprise Plans.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "ClickUp Public API v3",
    "version": "version",
    "description": "This API is exposed to the public internet and is meant to be accessed by third-party integrations."
  },
  "servers": [
    {
      "url": "https://api.clickup.com/",
      "description": "ClickUp"
    }
  ],
  "paths": {
    "/api/v3/workspaces/{workspace_id}/auditlogs": {
      "post": {
        "operationId": "queryAuditLog",
        "summary": "Create Workspace-level audit logs",
        "description": "Create Workspace-level audit logs. Audit logs can only be created by the Workspace owner on Enterprise Plans.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "required": true,
            "schema": {
              "description": "The ID of the Workspace.",
              "type": "number",
              "x-readme-ref-name": "AutoAuditlogWorkspaceAuditLogPublicControllerQueryAuditLogWorkspaceIdPath"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "filter": {
                    "description": "A filter containing the criteria to filter logs by.",
                    "allOf": [
                      {
                        "type": "object",
                        "properties": {
                          "workspaceId": {
                            "description": "The ID of the Workspace.",
                            "type": "object"
                          },
                          "userId": {
                            "description": "The user ID. This can be a single user or multiple.",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "userEmail": {
                            "description": "User emails. This can be a single email or multiple.",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "eventType": {
                            "description": "Types of events to filter by. Options include `USER_LOGIN`, `USER_LOGOUT`, `CHANGE_2FA`, `CHANGE_PASSWORD`, `CHANGE_EMAIL`, `JOIN_WORKSPACE`, `LEAVE_WORKSPACE`, `REMOVE_FROM_WORKSPACE`, `RESET_PASSWORD`, `ROLE_CHANGE`, `SCIM_PROVISION`, `SCIM_DEPROVISION`, `SCIM_UPDATE`, `ADVANCED_SETTINGS_UPDATED`, `CHANGE_ROLE_PERMISSIONS`, `INVITE_TO_WORKSPACE`, `CHANGE_USER_ROLE`, `CHANGE_SSO_POLICY`, `CHANGE_2FA_POLICY`, `CUSTOM_ROLE_CREATED`, `CUSTOM_ROLE_UPDATED`, `CUSTOM_ROLE_DELETED`, `SCIM_GROUP_CREATED`, `SCIM_GROUP_UPDATED`, `SCIM_GROUP_DELETED`, `TEAM_CREATED`, `TEAM_DELETED`, `TEAM_EDITED`, `TEAM_MEMBER_ADDED`, `TEAM_MEMBER_REMOVED`, `SSO_CONFIG_UPDATED`, `TASK_CREATED`, `TASK_ARCHIVED`, `TASK_DELETED`, `TASK_RESTORED`, `TASK_UNARCHIVED`, `TASK_STATUS_CHANGED`, `TASK_PRIORITY_CHANGED`, `TASK_ASSIGNEES_CHANGED`, and `TASK_CUSTOM_FIELD_VALUES_CHANGED`.",
                            "type": "string",
                            "enum": [
                              "USER_LOGIN",
                              "USER_LOGOUT",
                              "CHANGE_2FA",
                              "CHANGE_EMAIL",
                              "CHANGE_PASSWORD",
                              "JOIN_WORKSPACE",
                              "LEAVE_WORKSPACE",
                              "RESET_PASSWORD",
                              "ROLE_CHANGE",
                              "SCIM_DEPROVISION",
                              "SCIM_PROVISION",
                              "SCIM_UPDATE",
                              "SECURE_LOGIN_EMAIL_SENT",
                              "ADVANCED_SETTINGS_UPDATED",
                              "CHANGE_2FA_POLICY",
                              "CHANGE_ROLE_PERMISSIONS",
                              "CHANGE_SSO_POLICY",
                              "CHANGE_USER_ROLE",
                              "CUSTOM_ROLE_CREATED",
                              "CUSTOM_ROLE_DELETED",
                              "CUSTOM_ROLE_UPDATED",
                              "TEAM_CREATED",
                              "TEAM_DELETED",
                              "TEAM_EDITED",
                              "TEAM_MEMBER_ADDED",
                              "TEAM_MEMBER_REMOVED",
                              "INVITE_TO_WORKSPACE",
                              "REMOVE_FROM_WORKSPACE",
                              "SCIM_GROUP_CREATED",
                              "SCIM_GROUP_DELETED",
                              "SCIM_GROUP_UPDATED",
                              "SSO_CONFIG_UPDATED",
                              "TASK_ARCHIVED",
                              "TASK_ASSIGNEES_CHANGED",
                              "TASK_CREATED",
                              "TASK_CUSTOM_FIELD_VALUES_CHANGED",
                              "TASK_DELETED",
                              "TASK_PRIORITY_CHANGED",
                              "TASK_RESTORED",
                              "TASK_STATUS_CHANGED",
                              "TASK_UNARCHIVED",
                              "FIELD_CONVERTED",
                              "FIELD_CREATED",
                              "FIELD_DROPDOWN_OPTIONS_CREATED",
                              "FIELD_DROPDOWN_OPTIONS_REMOVED",
                              "FIELD_DROPDOWN_OPTIONS_UPDATED",
                              "FIELD_DUPLICATED",
                              "FIELD_GROUP_MEMBER_PERMISSION_REMOVED",
                              "FIELD_GROUP_MEMBER_PERMISSION_SET",
                              "FIELD_LABEL_OPTIONS_CREATED",
                              "FIELD_LABEL_OPTIONS_REMOVED",
                              "FIELD_LABEL_OPTIONS_UPDATED",
                              "FIELD_LOCATION_ADDED",
                              "FIELD_LOCATION_REMOVED",
                              "FIELD_LOCATION_UPDATED",
                              "FIELD_MEMBER_PERMISSION_REMOVED",
                              "FIELD_MEMBER_PERMISSION_SET",
                              "FIELD_MERGED",
                              "FIELD_PERMANENTLY_REMOVED",
                              "FIELD_REMOVED",
                              "FIELD_RESTORED",
                              "FIELD_UPDATED"
                            ]
                          },
                          "eventStatus": {
                            "description": "Status of events you're filtering by. Options include `success`, `failed`, `started`, `completed`, `error`, `system_error`.",
                            "type": "string",
                            "enum": [
                              "success",
                              "failed",
                              "started",
                              "completed",
                              "error",
                              "system_error"
                            ]
                          },
                          "startTime": {
                            "description": "The start time to begin paginating your logs.",
                            "type": "number"
                          },
                          "endTime": {
                            "description": "The end time to begin paginating your logs.",
                            "type": "number"
                          }
                        },
                        "x-readme-ref-name": "AutoAuditlogAuditEventFilterRequest"
                      }
                    ]
                  },
                  "applicability": {
                    "description": "Type of logs to filter by. Options include `auth-and-security`, `custom-fields`, `hierarchy-activity` and `user-activity`. Most use cases will use `auth-and-security`.",
                    "type": "string",
                    "enum": [
                      "auth-and-security",
                      "custom-fields",
                      "hierarchy-activity",
                      "user-activity"
                    ]
                  },
                  "pagination": {
                    "description": "The pagination request determines where logs should start and how many to return.",
                    "allOf": [
                      {
                        "type": "object",
                        "properties": {
                          "pageRows": {
                            "description": "The number of rows to return.",
                            "type": "number"
                          },
                          "pageTimestamp": {
                            "description": "The timestamp to index on. This should be the timestamp of the last row on the previous page. If you are requesting the first page, this should be the current timestamp.",
                            "type": "number"
                          },
                          "pageDirection": {
                            "description": "Pagination direction. This should be set to `before` for most use cases. Options include `before` and `after`."
                          }
                        },
                        "x-readme-ref-name": "AutoAuditlogAuditLogPaginationRequest"
                      }
                    ]
                  }
                },
                "x-readme-ref-name": "AutoAuditlogAuditLogQueryRequest"
              },
              "examples": {
                "Required": {
                  "value": {
                    "applicability": "auth-and-security"
                  }
                },
                "All": {
                  "value": {
                    "applicability": "auth-and-security",
                    "filter": {
                      "workspaceId": "123456",
                      "userId": [
                        "182"
                      ],
                      "userEmail": [
                        "user@company.com"
                      ],
                      "eventType": [
                        "CHANGE_PASSWORD"
                      ],
                      "eventStatus": "failed",
                      "startTime": 1718754539000,
                      "endTime": 1727221739000
                    },
                    "pagination": {
                      "pageRows": 10,
                      "pageTimestamp": 1727221739000,
                      "pageDirection": "before"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {}
            }
          }
        },
        "tags": [
          "Auditlogs",
          "Audit Logs"
        ],
        "x-is-workspace-endpoint": true
      }
    }
  },
  "components": {
    "securitySchemes": {
      "authHeader": {
        "in": "header",
        "type": "apiKey",
        "name": "Authorization"
      }
    }
  },
  "tags": [
    {
      "description": "Auditlogs API",
      "name": "Auditlogs"
    }
  ],
  "security": [
    {
      "authHeader": []
    }
  ]
}
```