# Update privacy and access of an object or location

Update the privacy and access settings of an object or location in the Workspace. Note that sharing an item may incur charges.

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
    "/api/v3/workspaces/{workspace_id}/{object_type}/{object_id}/acls": {
      "patch": {
        "operationId": "publicPatchAcl",
        "summary": "Update privacy and access of an object or location",
        "description": "Update the privacy and access settings of an object or location in the Workspace. Note that sharing an item may incur charges.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "required": true,
            "schema": {
              "description": "The ID of the Workspace.",
              "type": "number",
              "x-readme-ref-name": "UserAclPublicControllerPublicPatchAclWorkspaceIdPath"
            }
          },
          {
            "name": "object_type",
            "in": "path",
            "description": "ObjectType",
            "required": true,
            "schema": {
              "description": "Any object that can be shared in a Workspace. For example, `customField`, `dashboard`, `folder`, `goal`, `goalFolder`, `list`, `space`, `task`, and `view`.",
              "type": "string",
              "enum": [
                "attachment",
                "attachmentAccess",
                "approval",
                "banWorkspace",
                "checklist",
                "checklistItem",
                "checklistTemplateAccess",
                "comment",
                "commentsLastReadAt",
                "customField",
                "customFieldAccess",
                "customItem",
                "customPermissionLevel",
                "dashboard",
                "dashboardAccess",
                "doc",
                "docAccess",
                "folder",
                "folderDescendantsSet",
                "folderTemplateAccess",
                "form",
                "formulaValue",
                "foundationalJob",
                "goal",
                "goalAccess",
                "goalFolder",
                "goalFolderAccess",
                "hierarchy",
                "list",
                "listDescendantsSet",
                "listDescendantsPoints",
                "listDescendantsTimeEstimates",
                "listTemplateAccess",
                "notepad",
                "page",
                "pageAccess",
                "post",
                "reminder",
                "reminderAccess",
                "rolledUpFieldValue",
                "scheduledComment",
                "space",
                "spaceDescendantsSet",
                "spaceTemplateAccess",
                "task",
                "taskAccess",
                "taskHistory",
                "taskProperty",
                "taskTemplateAccess",
                "template",
                "user",
                "userAccess",
                "userGroup",
                "userHierarchy",
                "userPresence",
                "view",
                "viewAccess",
                "viewTemplateAccess",
                "whiteboard",
                "whiteboardAccess",
                "widget",
                "workspace",
                "workspaceDescendantsSet",
                "workscheduleWorkweekSchedule",
                "workscheduleScheduleExceptions"
              ],
              "x-readme-ref-name": "ObjectType"
            }
          },
          {
            "name": "object_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
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
                  "private": {
                    "description": "The privacy of an object or location.",
                    "type": "boolean"
                  },
                  "entries": {
                    "description": "The user or user group (Team) you wish to give, remove, or edit permissions.",
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "kind": {
                          "description": "The type of ID. Options are `user` or `group`.",
                          "type": "string",
                          "enum": [
                            "user",
                            "group"
                          ]
                        },
                        "id": {
                          "description": "The ID of user or user group (Team) you wish to give, remove, or edit permissions.",
                          "type": "string"
                        },
                        "permission_level": {
                          "description": "The permission level you wish to give to user or user group (Team). `1`=read, `3` = comment, `4`= edit, `5`= create, and `null`= remove access.",
                          "type": "number",
                          "enum": [
                            1,
                            3,
                            4,
                            5
                          ]
                        },
                        "from_group_id": {
                          "description": "If the user ACL entry was expanded from a group, this is the group's ID",
                          "type": "string"
                        },
                        "from_parent_type": {
                          "description": "Any object that can be shared in a Workspace. For example, `customField`, `dashboard`, `folder`, `goal`, `goalFolder`, `list`, `space`, `task`, and `view`.",
                          "type": "string",
                          "enum": [
                            "attachment",
                            "attachmentAccess",
                            "approval",
                            "banWorkspace",
                            "checklist",
                            "checklistItem",
                            "checklistTemplateAccess",
                            "comment",
                            "commentsLastReadAt",
                            "customField",
                            "customFieldAccess",
                            "customItem",
                            "customPermissionLevel",
                            "dashboard",
                            "dashboardAccess",
                            "doc",
                            "docAccess",
                            "folder",
                            "folderDescendantsSet",
                            "folderTemplateAccess",
                            "form",
                            "formulaValue",
                            "foundationalJob",
                            "goal",
                            "goalAccess",
                            "goalFolder",
                            "goalFolderAccess",
                            "hierarchy",
                            "list",
                            "listDescendantsSet",
                            "listDescendantsPoints",
                            "listDescendantsTimeEstimates",
                            "listTemplateAccess",
                            "notepad",
                            "page",
                            "pageAccess",
                            "post",
                            "reminder",
                            "reminderAccess",
                            "rolledUpFieldValue",
                            "scheduledComment",
                            "space",
                            "spaceDescendantsSet",
                            "spaceTemplateAccess",
                            "task",
                            "taskAccess",
                            "taskHistory",
                            "taskProperty",
                            "taskTemplateAccess",
                            "template",
                            "user",
                            "userAccess",
                            "userGroup",
                            "userHierarchy",
                            "userPresence",
                            "view",
                            "viewAccess",
                            "viewTemplateAccess",
                            "whiteboard",
                            "whiteboardAccess",
                            "widget",
                            "workspace",
                            "workspaceDescendantsSet",
                            "workscheduleWorkweekSchedule",
                            "workscheduleScheduleExceptions"
                          ],
                          "x-readme-ref-name": "ObjectType"
                        },
                        "from_parent_id": {
                          "description": "If set, this ACL entry was expanded from a parent with this id.  Will be undefined if parent is not accessible.",
                          "type": "string"
                        },
                        "calculated": {
                          "description": "If set, this ACL entry was calculated from the user's attributes (e.g. the user is the owner of the object)",
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "kind",
                        "id"
                      ],
                      "x-readme-ref-name": "UserAclEntry"
                    }
                  }
                },
                "x-readme-ref-name": "UserPatchAclApiRequest"
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
          "Acls",
          "Privacy and access"
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
      "description": "Acls API",
      "name": "Acls"
    }
  ],
  "security": [
    {
      "authHeader": []
    }
  ]
}
```