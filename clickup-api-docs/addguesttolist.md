# Add Guest To List

Share a List with a guest. \
 \
***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/list/{list_id}/guest/{guest_id}": {
      "post": {
        "summary": "Add Guest To List",
        "tags": [
          "Guests"
        ],
        "description": "Share a List with a guest. \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "AddGuestToList",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                1427
              ]
            }
          },
          {
            "name": "guest_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                403
              ]
            }
          },
          {
            "name": "include_shared",
            "in": "query",
            "description": "Exclude details of items shared with the guest by setting this parameter to `false`. By default this parameter is set to `true`.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                false
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "AddGuestToListrequest",
                "required": [
                  "permission_level"
                ],
                "type": "object",
                "properties": {
                  "permission_level": {
                    "description": "Can be `read` (view only), `comment`, `edit`, or `create` (full).",
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "permission_level": "read"
                  }
                ]
              },
              "example": {
                "permission_level": "read"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "AddGuestToListresponse",
                  "required": [
                    "guest"
                  ],
                  "type": "object",
                  "properties": {
                    "guest": {
                      "title": "Guest3",
                      "required": [
                        "user",
                        "invited_by",
                        "can_see_time_spent",
                        "can_see_time_estimated",
                        "can_edit_tags",
                        "shared"
                      ],
                      "type": "object",
                      "properties": {
                        "user": {
                          "title": "User7",
                          "required": [
                            "id",
                            "username",
                            "email",
                            "color",
                            "profilePicture",
                            "initials",
                            "role",
                            "last_active",
                            "date_joined",
                            "date_invited"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "username": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "email": {
                              "type": "string"
                            },
                            "color": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "profilePicture": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "initials": {
                              "type": "string"
                            },
                            "role": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "last_active": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "date_joined": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "date_invited": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "id": 184,
                              "username": null,
                              "email": "guest@example.com",
                              "color": null,
                              "profilePicture": null,
                              "initials": "G",
                              "role": 4,
                              "last_active": null,
                              "date_joined": null,
                              "date_invited": "1583358383412"
                            }
                          ]
                        },
                        "invited_by": {
                          "title": "InvitedBy",
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "color": {
                              "type": "string"
                            },
                            "username": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "initials": {
                              "type": "string"
                            },
                            "profilePicture": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "id": 183,
                              "color": "#827718",
                              "username": "Jerry",
                              "email": "jerry@example.com",
                              "initials": "J",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                            }
                          ]
                        },
                        "can_see_time_spent": {
                          "type": "boolean"
                        },
                        "can_see_time_estimated": {
                          "type": "boolean"
                        },
                        "can_edit_tags": {
                          "type": "boolean"
                        },
                        "shared": {
                          "title": "Shared3",
                          "required": [
                            "tasks",
                            "lists",
                            "folders"
                          ],
                          "type": "object",
                          "properties": {
                            "tasks": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              },
                              "description": ""
                            },
                            "lists": {
                              "type": "array",
                              "items": {
                                "title": "List3",
                                "required": [
                                  "id",
                                  "name",
                                  "orderindex",
                                  "status",
                                  "priority",
                                  "assignee",
                                  "task_count",
                                  "due_date",
                                  "start_date",
                                  "archived",
                                  "override_statuses",
                                  "statuses",
                                  "permission_level"
                                ],
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "string"
                                  },
                                  "name": {
                                    "type": "string"
                                  },
                                  "orderindex": {
                                    "type": "integer",
                                    "contentEncoding": "int32"
                                  },
                                  "status": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "priority": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "assignee": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "task_count": {
                                    "type": "string"
                                  },
                                  "due_date": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "start_date": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "archived": {
                                    "type": "boolean"
                                  },
                                  "override_statuses": {
                                    "type": "boolean"
                                  },
                                  "statuses": {
                                    "type": "array",
                                    "items": {
                                      "title": "Status",
                                      "type": "object",
                                      "properties": {
                                        "id": {
                                          "type": "string"
                                        },
                                        "status": {
                                          "type": "string"
                                        },
                                        "color": {
                                          "type": "string"
                                        },
                                        "orderindex": {
                                          "type": "integer",
                                          "contentEncoding": "int32"
                                        },
                                        "type": {
                                          "type": "string"
                                        }
                                      },
                                      "examples": [
                                        {
                                          "id": "p7001234_FxGmgrnk",
                                          "status": "in progress",
                                          "color": "#d3d3d3",
                                          "orderindex": 1,
                                          "type": "custom"
                                        }
                                      ]
                                    },
                                    "description": ""
                                  },
                                  "permission_level": {
                                    "type": "string"
                                  }
                                },
                                "examples": [
                                  {
                                    "id": "1427",
                                    "name": "List Name",
                                    "orderindex": 1,
                                    "status": null,
                                    "priority": null,
                                    "assignee": null,
                                    "task_count": "5",
                                    "due_date": null,
                                    "start_date": null,
                                    "archived": false,
                                    "override_statuses": true,
                                    "statuses": [
                                      {
                                        "status": "Open",
                                        "orderindex": 0,
                                        "color": "#d3d3d3",
                                        "type": "open"
                                      },
                                      {
                                        "status": "Closed",
                                        "orderindex": 5,
                                        "color": "#6bc950",
                                        "type": "closed"
                                      }
                                    ],
                                    "permission_level": "read"
                                  }
                                ]
                              },
                              "description": ""
                            },
                            "folders": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              },
                              "description": ""
                            }
                          },
                          "examples": [
                            {
                              "tasks": [],
                              "lists": [
                                {
                                  "id": "1427",
                                  "name": "List Name",
                                  "orderindex": 1,
                                  "status": null,
                                  "priority": null,
                                  "assignee": null,
                                  "task_count": "5",
                                  "due_date": null,
                                  "start_date": null,
                                  "archived": false,
                                  "override_statuses": true,
                                  "statuses": [
                                    {
                                      "status": "Open",
                                      "orderindex": 0,
                                      "color": "#d3d3d3",
                                      "type": "open"
                                    },
                                    {
                                      "status": "Closed",
                                      "orderindex": 5,
                                      "color": "#6bc950",
                                      "type": "closed"
                                    }
                                  ],
                                  "permission_level": "read"
                                }
                              ],
                              "folders": []
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "user": {
                            "id": 184,
                            "username": null,
                            "email": "guest@example.com",
                            "color": null,
                            "profilePicture": null,
                            "initials": "G",
                            "role": 4,
                            "last_active": null,
                            "date_joined": null,
                            "date_invited": "1583358383412"
                          },
                          "invited_by": {
                            "id": 183,
                            "color": "#827718",
                            "username": "Jerry",
                            "email": "jerry@example.com",
                            "initials": "J",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                          },
                          "can_see_time_spent": true,
                          "can_see_time_estimated": true,
                          "can_edit_tags": true,
                          "shared": {
                            "tasks": [],
                            "lists": [
                              {
                                "id": "1427",
                                "name": "List Name",
                                "orderindex": 1,
                                "status": null,
                                "priority": null,
                                "assignee": null,
                                "task_count": "5",
                                "due_date": null,
                                "start_date": null,
                                "archived": false,
                                "override_statuses": true,
                                "statuses": [
                                  {
                                    "status": "Open",
                                    "orderindex": 0,
                                    "color": "#d3d3d3",
                                    "type": "open"
                                  },
                                  {
                                    "status": "Closed",
                                    "orderindex": 5,
                                    "color": "#6bc950",
                                    "type": "closed"
                                  }
                                ],
                                "permission_level": "read"
                              }
                            ],
                            "folders": []
                          }
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "guest": {
                        "user": {
                          "id": 184,
                          "username": null,
                          "email": "guest@example.com",
                          "color": null,
                          "profilePicture": null,
                          "initials": "G",
                          "role": 4,
                          "last_active": null,
                          "date_joined": null,
                          "date_invited": "1583358383412"
                        },
                        "invited_by": {
                          "id": 183,
                          "color": "#827718",
                          "username": "Jerry",
                          "email": "jerry@example.com",
                          "initials": "J",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                        },
                        "can_see_time_spent": true,
                        "can_see_time_estimated": true,
                        "can_edit_tags": true,
                        "shared": {
                          "tasks": [],
                          "lists": [
                            {
                              "id": "1427",
                              "name": "List Name",
                              "orderindex": 1,
                              "status": null,
                              "priority": null,
                              "assignee": null,
                              "task_count": "5",
                              "due_date": null,
                              "start_date": null,
                              "archived": false,
                              "override_statuses": true,
                              "statuses": [
                                {
                                  "status": "Open",
                                  "orderindex": 0,
                                  "color": "#d3d3d3",
                                  "type": "open"
                                },
                                {
                                  "status": "Closed",
                                  "orderindex": 5,
                                  "color": "#6bc950",
                                  "type": "closed"
                                }
                              ],
                              "permission_level": "read"
                            }
                          ],
                          "folders": []
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "guest": {
                    "user": {
                      "id": 184,
                      "username": null,
                      "email": "guest@example.com",
                      "color": null,
                      "profilePicture": null,
                      "initials": "G",
                      "role": 4,
                      "last_active": null,
                      "date_joined": null,
                      "date_invited": "1583358383412"
                    },
                    "invited_by": {
                      "id": 183,
                      "color": "#827718",
                      "username": "Jerry",
                      "email": "jerry@example.com",
                      "initials": "J",
                      "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                    },
                    "can_see_time_spent": true,
                    "can_see_time_estimated": true,
                    "can_edit_tags": true,
                    "shared": {
                      "tasks": [],
                      "lists": [
                        {
                          "id": "1427",
                          "name": "List Name",
                          "orderindex": 1,
                          "status": null,
                          "priority": null,
                          "assignee": null,
                          "task_count": "5",
                          "due_date": null,
                          "start_date": null,
                          "archived": false,
                          "override_statuses": true,
                          "statuses": [
                            {
                              "status": "Open",
                              "orderindex": 0,
                              "color": "#d3d3d3",
                              "type": "open"
                            },
                            {
                              "status": "Closed",
                              "orderindex": 5,
                              "color": "#6bc950",
                              "type": "closed"
                            }
                          ],
                          "permission_level": "read"
                        }
                      ],
                      "folders": []
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Guests"
    }
  ]
}
```