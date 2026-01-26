# Add Guest To Task

Share a task with a guest. \
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
    "/v2/task/{task_id}/guest/{guest_id}": {
      "post": {
        "summary": "Add Guest To Task",
        "tags": [
          "Guests"
        ],
        "description": "Share a task with a guest. \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "AddGuestToTask",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "c04"
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
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by it's custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "AddGuestToTaskrequest",
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
                  "title": "AddGuestToTaskresponse",
                  "required": [
                    "guest"
                  ],
                  "type": "object",
                  "properties": {
                    "guest": {
                      "title": "Guest1",
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
                          "title": "Shared1",
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
                                "title": "Task2",
                                "required": [
                                  "id",
                                  "name",
                                  "status",
                                  "orderindex",
                                  "date_created",
                                  "date_updated",
                                  "date_closed",
                                  "archived",
                                  "creator",
                                  "assignees",
                                  "checklists",
                                  "tags",
                                  "parent",
                                  "priority",
                                  "due_date",
                                  "start_date",
                                  "points",
                                  "time_estimate",
                                  "custom_fields",
                                  "dependencies",
                                  "team_id",
                                  "url",
                                  "permission_level",
                                  "list",
                                  "folder",
                                  "space"
                                ],
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "string"
                                  },
                                  "name": {
                                    "type": "string"
                                  },
                                  "status": {
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
                                  "orderindex": {
                                    "type": "string"
                                  },
                                  "date_created": {
                                    "type": "string"
                                  },
                                  "date_updated": {
                                    "type": "string"
                                  },
                                  "date_closed": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "archived": {
                                    "type": "boolean"
                                  },
                                  "creator": {
                                    "title": "Creator",
                                    "required": [
                                      "id",
                                      "username",
                                      "color",
                                      "profilePicture"
                                    ],
                                    "type": "object",
                                    "properties": {
                                      "id": {
                                        "type": "integer",
                                        "contentEncoding": "int32"
                                      },
                                      "username": {
                                        "type": "string"
                                      },
                                      "color": {
                                        "type": "string"
                                      },
                                      "profilePicture": {
                                        "type": "string"
                                      }
                                    },
                                    "examples": [
                                      {
                                        "id": 183,
                                        "username": "John Doe",
                                        "color": "#827718",
                                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                                      }
                                    ]
                                  },
                                  "assignees": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "description": ""
                                  },
                                  "checklists": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "description": ""
                                  },
                                  "tags": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "description": ""
                                  },
                                  "parent": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "priority": {
                                    "title": "Priority",
                                    "type": "object",
                                    "nullable": true,
                                    "properties": {
                                      "color": {
                                        "type": "string"
                                      },
                                      "id": {
                                        "type": "string"
                                      },
                                      "orderindex": {
                                        "type": "string"
                                      },
                                      "priority": {
                                        "type": "string"
                                      }
                                    },
                                    "examples": [
                                      {
                                        "color": "#f8ae00",
                                        "id": "3",
                                        "orderindex": "3",
                                        "priority": "normal"
                                      }
                                    ]
                                  },
                                  "due_date": {
                                    "type": "string"
                                  },
                                  "start_date": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "points": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "time_estimate": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "custom_fields": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "description": ""
                                  },
                                  "dependencies": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "description": ""
                                  },
                                  "team_id": {
                                    "type": "string"
                                  },
                                  "url": {
                                    "type": "string"
                                  },
                                  "permission_level": {
                                    "type": "string"
                                  },
                                  "list": {
                                    "title": "List2",
                                    "required": [
                                      "id",
                                      "name",
                                      "access"
                                    ],
                                    "type": "object",
                                    "properties": {
                                      "id": {
                                        "type": "string"
                                      },
                                      "name": {
                                        "type": "string"
                                      },
                                      "access": {
                                        "type": "boolean"
                                      }
                                    },
                                    "examples": [
                                      {
                                        "id": "1752",
                                        "name": "Shared with me",
                                        "access": false
                                      }
                                    ]
                                  },
                                  "folder": {
                                    "title": "Folder3",
                                    "required": [
                                      "id",
                                      "name",
                                      "hidden",
                                      "access"
                                    ],
                                    "type": "object",
                                    "properties": {
                                      "id": {
                                        "type": "string"
                                      },
                                      "name": {
                                        "type": "string"
                                      },
                                      "hidden": {
                                        "type": "boolean"
                                      },
                                      "access": {
                                        "type": "boolean"
                                      }
                                    },
                                    "examples": [
                                      {
                                        "id": "1217",
                                        "name": "Shared with me",
                                        "hidden": false,
                                        "access": false
                                      }
                                    ]
                                  },
                                  "space": {
                                    "title": "Space",
                                    "required": [
                                      "id"
                                    ],
                                    "type": "object",
                                    "properties": {
                                      "id": {
                                        "type": "string"
                                      }
                                    },
                                    "examples": [
                                      {
                                        "id": "789"
                                      }
                                    ]
                                  }
                                },
                                "examples": [
                                  {
                                    "id": "c04",
                                    "name": "Task Name",
                                    "status": {
                                      "status": "Open",
                                      "color": "#d3d3d3",
                                      "type": "open",
                                      "orderindex": 0
                                    },
                                    "orderindex": "0",
                                    "date_created": "1574718405408",
                                    "date_updated": "1574722145869",
                                    "date_closed": null,
                                    "archived": false,
                                    "creator": {
                                      "id": 183,
                                      "username": "Jerry",
                                      "color": "#827718",
                                      "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                                    },
                                    "assignees": [],
                                    "checklists": [],
                                    "tags": [],
                                    "parent": null,
                                    "priority": {
                                      "id": "1",
                                      "priority": "urgent",
                                      "color": "#f50000",
                                      "orderindex": "1"
                                    },
                                    "due_date": "1508369194377",
                                    "start_date": null,
                                    "points": null,
                                    "time_estimate": null,
                                    "custom_fields": [],
                                    "dependencies": [],
                                    "team_id": "108",
                                    "url": "https://app.clickup.com/t/c04",
                                    "permission_level": "read",
                                    "list": {
                                      "id": "1752",
                                      "name": "Shared with me",
                                      "access": false
                                    },
                                    "folder": {
                                      "id": "1217",
                                      "name": "Shared with me",
                                      "hidden": false,
                                      "access": false
                                    },
                                    "space": {
                                      "id": "380"
                                    }
                                  }
                                ]
                              },
                              "description": ""
                            },
                            "lists": {
                              "type": "array",
                              "items": {
                                "type": "string"
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
                              "tasks": [
                                {
                                  "id": "c04",
                                  "name": "Task Name",
                                  "status": {
                                    "status": "Open",
                                    "color": "#d3d3d3",
                                    "type": "open",
                                    "orderindex": 0
                                  },
                                  "orderindex": "0",
                                  "date_created": "1574718405408",
                                  "date_updated": "1574722145869",
                                  "date_closed": null,
                                  "archived": false,
                                  "creator": {
                                    "id": 183,
                                    "username": "Jerry",
                                    "color": "#827718",
                                    "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                                  },
                                  "assignees": [],
                                  "checklists": [],
                                  "tags": [],
                                  "parent": null,
                                  "priority": {
                                    "id": "1",
                                    "priority": "urgent",
                                    "color": "#f50000",
                                    "orderindex": "1"
                                  },
                                  "due_date": "1508369194377",
                                  "start_date": null,
                                  "points": null,
                                  "time_estimate": null,
                                  "custom_fields": [],
                                  "dependencies": [],
                                  "team_id": "108",
                                  "url": "https://app.clickup.com/t/c04",
                                  "permission_level": "read",
                                  "list": {
                                    "id": "1752",
                                    "name": "Shared with me",
                                    "access": false
                                  },
                                  "folder": {
                                    "id": "1217",
                                    "name": "Shared with me",
                                    "hidden": false,
                                    "access": false
                                  },
                                  "space": {
                                    "id": "380"
                                  }
                                }
                              ],
                              "lists": [],
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
                            "tasks": [
                              {
                                "id": "c04",
                                "name": "Task Name",
                                "status": {
                                  "status": "Open",
                                  "color": "#d3d3d3",
                                  "type": "open",
                                  "orderindex": 0
                                },
                                "orderindex": "0",
                                "date_created": "1574718405408",
                                "date_updated": "1574722145869",
                                "date_closed": null,
                                "archived": false,
                                "creator": {
                                  "id": 183,
                                  "username": "Jerry",
                                  "color": "#827718",
                                  "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                                },
                                "assignees": [],
                                "checklists": [],
                                "tags": [],
                                "parent": null,
                                "priority": {
                                  "id": "1",
                                  "priority": "urgent",
                                  "color": "#f50000",
                                  "orderindex": "1"
                                },
                                "due_date": "1508369194377",
                                "start_date": null,
                                "points": null,
                                "time_estimate": null,
                                "custom_fields": [],
                                "dependencies": [],
                                "team_id": "108",
                                "url": "https://app.clickup.com/t/c04",
                                "permission_level": "read",
                                "list": {
                                  "id": "1752",
                                  "name": "Shared with me",
                                  "access": false
                                },
                                "folder": {
                                  "id": "1217",
                                  "name": "Shared with me",
                                  "hidden": false,
                                  "access": false
                                },
                                "space": {
                                  "id": "380"
                                }
                              }
                            ],
                            "lists": [],
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
                          "tasks": [
                            {
                              "id": "c04",
                              "name": "Task Name",
                              "status": {
                                "status": "Open",
                                "color": "#d3d3d3",
                                "type": "open",
                                "orderindex": 0
                              },
                              "orderindex": "0",
                              "date_created": "1574718405408",
                              "date_updated": "1574722145869",
                              "date_closed": null,
                              "archived": false,
                              "creator": {
                                "id": 183,
                                "username": "Jerry",
                                "color": "#827718",
                                "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                              },
                              "assignees": [],
                              "checklists": [],
                              "tags": [],
                              "parent": null,
                              "priority": {
                                "id": "1",
                                "priority": "urgent",
                                "color": "#f50000",
                                "orderindex": "1"
                              },
                              "due_date": "1508369194377",
                              "start_date": null,
                              "points": null,
                              "time_estimate": null,
                              "custom_fields": [],
                              "dependencies": [],
                              "team_id": "108",
                              "url": "https://app.clickup.com/t/c04",
                              "permission_level": "read",
                              "list": {
                                "id": "1752",
                                "name": "Shared with me",
                                "access": false
                              },
                              "folder": {
                                "id": "1217",
                                "name": "Shared with me",
                                "hidden": false,
                                "access": false
                              },
                              "space": {
                                "id": "380"
                              }
                            }
                          ],
                          "lists": [],
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
                      "tasks": [
                        {
                          "id": "c04",
                          "name": "Task Name",
                          "status": {
                            "status": "Open",
                            "color": "#d3d3d3",
                            "type": "open",
                            "orderindex": 0
                          },
                          "orderindex": "0",
                          "date_created": "1574718405408",
                          "date_updated": "1574722145869",
                          "date_closed": null,
                          "archived": false,
                          "creator": {
                            "id": 183,
                            "username": "Jerry",
                            "color": "#827718",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                          },
                          "assignees": [],
                          "checklists": [],
                          "tags": [],
                          "parent": null,
                          "priority": {
                            "id": "1",
                            "priority": "urgent",
                            "color": "#f50000",
                            "orderindex": "1"
                          },
                          "due_date": "1508369194377",
                          "start_date": null,
                          "points": null,
                          "time_estimate": null,
                          "custom_fields": [],
                          "dependencies": [],
                          "team_id": "108",
                          "url": "https://app.clickup.com/t/c04",
                          "permission_level": "read",
                          "list": {
                            "id": "1752",
                            "name": "Shared with me",
                            "access": false
                          },
                          "folder": {
                            "id": "1217",
                            "name": "Shared with me",
                            "hidden": false,
                            "access": false
                          },
                          "space": {
                            "id": "380"
                          }
                        }
                      ],
                      "lists": [],
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