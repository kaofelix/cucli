# Get singular time entry

View a single time entry. \
 \
***Note:** A time entry that has a negative duration means that timer is currently running for that user.*

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
    "/v2/team/{team_id}/time_entries/{timer_id}": {
      "get": {
        "summary": "Get singular time entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "View a single time entry. \\\n \\\n***Note:** A time entry that has a negative duration means that timer is currently running for that user.*",
        "operationId": "Getsingulartimeentry",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "timer_id",
            "in": "path",
            "description": "The ID of a time entry. \\\n \\\nThis can be found using the [Get Time Entries Within a Date Range](https://developer.clickup.com/reference/gettimeentrieswithinadaterange) endpoint.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "1963465985517105840"
              ]
            }
          },
          {
            "name": "include_task_tags",
            "in": "query",
            "description": "Include task tags in the response for time entries associated with tasks.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_location_names",
            "in": "query",
            "description": "Include the names of the List, Folder, and Space along with `list_id`,`folder_id`, and `space_id`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_approval_history",
            "in": "query",
            "description": "Include the history of the approval for the time entry.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_approval_details",
            "in": "query",
            "description": "Include the details of the approval for the time entry.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "Content-Type",
            "in": "header",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "const": "application/json",
              "type": "string",
              "examples": [
                "application/json"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "Getsingulartimeentryresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "description": "",
                      "title": "Datum2",
                      "required": [
                        "id",
                        "wid",
                        "user",
                        "billable",
                        "start",
                        "end",
                        "duration",
                        "description",
                        "tags",
                        "source",
                        "at",
                        "task_location",
                        "task_tags",
                        "task_url"
                      ],
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "wid": {
                          "type": "string"
                        },
                        "user": {
                          "title": "User2",
                          "required": [
                            "id",
                            "username",
                            "initials",
                            "email",
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
                            "initials": {
                              "type": "string"
                            },
                            "email": {
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
                              "initials": "JD",
                              "email": "johndoe@gmail.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            }
                          ]
                        },
                        "billable": {
                          "type": "boolean"
                        },
                        "start": {
                          "type": "string"
                        },
                        "end": {
                          "type": "string"
                        },
                        "duration": {
                          "type": "string"
                        },
                        "description": {
                          "type": "string"
                        },
                        "tags": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "source": {
                          "type": "string"
                        },
                        "at": {
                          "type": "string"
                        },
                        "approval_id": {
                          "type": "string",
                          "description": "ID of the associated approval"
                        },
                        "approval": {
                          "title": "Approval",
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "description": "Unique identifier for the approval"
                            },
                            "workspace_id": {
                              "type": "integer",
                              "description": "ID of the workspace this approval belongs to"
                            },
                            "status": {
                              "type": "string",
                              "description": "Current status of the approval (e.g., 'approved', 'pending')"
                            },
                            "data": {
                              "type": "object",
                              "properties": {
                                "end_of_week": {
                                  "type": "integer",
                                  "description": "Timestamp for the end of the week"
                                },
                                "start_of_week": {
                                  "type": "integer",
                                  "description": "Timestamp for the start of the week"
                                }
                              }
                            },
                            "user": {
                              "title": "User13",
                              "required": [
                                "id",
                                "username",
                                "email",
                                "color",
                                "initials",
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
                                "email": {
                                  "type": "string"
                                },
                                "color": {
                                  "type": "string"
                                },
                                "initials": {
                                  "type": "string"
                                },
                                "profilePicture": {
                                  "type": [
                                    "string",
                                    "null"
                                  ]
                                }
                              },
                              "examples": [
                                {
                                  "id": 1,
                                  "username": "John Doe",
                                  "email": "johndoe@gmail.com",
                                  "color": "#795548",
                                  "initials": "JD",
                                  "profilePicture": null
                                }
                              ]
                            },
                            "approvers": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "integer",
                                    "description": "ID of the user who can approve the request"
                                  }
                                }
                              }
                            },
                            "approver_id": {
                              "type": "integer",
                              "description": "ID of the user who approved the request"
                            },
                            "approved_at": {
                              "type": "integer",
                              "description": "Timestamp when the approval was granted"
                            },
                            "history": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "string",
                                    "description": "Unique identifier for the history entry"
                                  },
                                  "field": {
                                    "type": "string",
                                    "description": "Field that was changed"
                                  },
                                  "before": {
                                    "type": "string",
                                    "description": "Previous value"
                                  },
                                  "after": {
                                    "type": "string",
                                    "description": "New value"
                                  },
                                  "created_at": {
                                    "type": "integer",
                                    "description": "Timestamp when the change was made"
                                  },
                                  "user": {
                                    "title": "User13",
                                    "required": [
                                      "id",
                                      "username",
                                      "email",
                                      "color",
                                      "initials",
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
                                      "email": {
                                        "type": "string"
                                      },
                                      "color": {
                                        "type": "string"
                                      },
                                      "initials": {
                                        "type": "string"
                                      },
                                      "profilePicture": {
                                        "type": [
                                          "string",
                                          "null"
                                        ]
                                      }
                                    },
                                    "examples": [
                                      {
                                        "id": 1,
                                        "username": "John Doe",
                                        "email": "johndoe@gmail.com",
                                        "color": "#795548",
                                        "initials": "JD",
                                        "profilePicture": null
                                      }
                                    ]
                                  }
                                }
                              }
                            }
                          },
                          "examples": [
                            {
                              "id": "123e4567-e89b-12d3-a456-426614174000",
                              "workspace_id": 12345,
                              "status": "approved",
                              "data": {
                                "end_of_week": 1672531199000,
                                "start_of_week": 1671926400000
                              },
                              "user": {
                                "id": 101,
                                "username": "john.smith",
                                "initials": "JS",
                                "avatar": {
                                  "color": "#4287f5",
                                  "picture_url": null
                                }
                              },
                              "approvers": [
                                {
                                  "id": 101
                                },
                                {
                                  "id": 102
                                }
                              ],
                              "approver_id": 101,
                              "approved_at": 1672012800000,
                              "history": [
                                {
                                  "id": "987fcdeb-51a2-3456-789a-bcdef0123456",
                                  "field": "submission",
                                  "before": null,
                                  "after": null,
                                  "created_at": 1671987600000,
                                  "user": {
                                    "id": 101,
                                    "username": "john.smith",
                                    "role": "submitter"
                                  }
                                },
                                {
                                  "id": "456abcde-f123-4567-89ab-cdef01234567",
                                  "field": "status",
                                  "before": "pending",
                                  "after": "approved",
                                  "created_at": 1672012800000,
                                  "user": {
                                    "id": 102,
                                    "username": "jane.doe",
                                    "role": "approver"
                                  }
                                }
                              ]
                            }
                          ]
                        },
                        "task_location": {
                          "title": "TaskLocation",
                          "required": [
                            "list_id",
                            "folder_id",
                            "space_id",
                            "list_name",
                            "folder_name",
                            "space_name"
                          ],
                          "type": "object",
                          "properties": {
                            "list_id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "folder_id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "space_id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "list_name": {
                              "type": "string"
                            },
                            "folder_name": {
                              "type": "string"
                            },
                            "space_name": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "list_id": 1560300071,
                              "folder_id": 468300080,
                              "space_id": 22800253,
                              "list_name": "List",
                              "folder_name": "Folder",
                              "space_name": "Space"
                            }
                          ]
                        },
                        "task_tags": {
                          "type": "array",
                          "items": {
                            "title": "TaskTag",
                            "required": [
                              "name",
                              "tag_fg",
                              "tag_bg",
                              "creator"
                            ],
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": "string"
                              },
                              "tag_fg": {
                                "type": "string"
                              },
                              "tag_bg": {
                                "type": "string"
                              },
                              "creator": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              }
                            },
                            "examples": [
                              {
                                "name": "content-request",
                                "tag_fg": "#800000",
                                "tag_bg": "#2ecd6f",
                                "creator": 301828
                              }
                            ]
                          },
                          "description": ""
                        },
                        "task_url": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "timer_id",
                          "wid": "workspace_id",
                          "user": {
                            "id": 1,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": "1592841559129",
                          "end": "1592845899021",
                          "duration": "4339892",
                          "description": "",
                          "tags": [],
                          "source": "clickup",
                          "at": "1592845899021",
                          "approval_id": "2d539936-119a-4927-9770-179f0a72e2e5",
                          "approval": {
                            "title": "Approval",
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "Unique identifier for the approval"
                              },
                              "workspace_id": {
                                "type": "integer",
                                "description": "ID of the workspace this approval belongs to"
                              },
                              "status": {
                                "type": "string",
                                "description": "Current status of the approval (e.g., 'approved', 'pending')"
                              },
                              "data": {
                                "type": "object",
                                "properties": {
                                  "end_of_week": {
                                    "type": "integer",
                                    "description": "Timestamp for the end of the week"
                                  },
                                  "start_of_week": {
                                    "type": "integer",
                                    "description": "Timestamp for the start of the week"
                                  }
                                }
                              },
                              "user": {
                                "title": "User13",
                                "required": [
                                  "id",
                                  "username",
                                  "email",
                                  "color",
                                  "initials",
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
                                  "email": {
                                    "type": "string"
                                  },
                                  "color": {
                                    "type": "string"
                                  },
                                  "initials": {
                                    "type": "string"
                                  },
                                  "profilePicture": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  }
                                },
                                "examples": [
                                  {
                                    "id": 1,
                                    "username": "John Doe",
                                    "email": "johndoe@gmail.com",
                                    "color": "#795548",
                                    "initials": "JD",
                                    "profilePicture": null
                                  }
                                ]
                              },
                              "approvers": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer",
                                      "description": "ID of the user who can approve the request"
                                    }
                                  }
                                }
                              },
                              "approver_id": {
                                "type": "integer",
                                "description": "ID of the user who approved the request"
                              },
                              "approved_at": {
                                "type": "integer",
                                "description": "Timestamp when the approval was granted"
                              },
                              "history": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "string",
                                      "description": "Unique identifier for the history entry"
                                    },
                                    "field": {
                                      "type": "string",
                                      "description": "Field that was changed"
                                    },
                                    "before": {
                                      "type": "string",
                                      "description": "Previous value"
                                    },
                                    "after": {
                                      "type": "string",
                                      "description": "New value"
                                    },
                                    "created_at": {
                                      "type": "integer",
                                      "description": "Timestamp when the change was made"
                                    },
                                    "user": {
                                      "title": "User13",
                                      "required": [
                                        "id",
                                        "username",
                                        "email",
                                        "color",
                                        "initials",
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
                                        "email": {
                                          "type": "string"
                                        },
                                        "color": {
                                          "type": "string"
                                        },
                                        "initials": {
                                          "type": "string"
                                        },
                                        "profilePicture": {
                                          "type": [
                                            "string",
                                            "null"
                                          ]
                                        }
                                      },
                                      "examples": [
                                        {
                                          "id": 1,
                                          "username": "John Doe",
                                          "email": "johndoe@gmail.com",
                                          "color": "#795548",
                                          "initials": "JD",
                                          "profilePicture": null
                                        }
                                      ]
                                    }
                                  }
                                }
                              }
                            },
                            "examples": [
                              {
                                "id": "123e4567-e89b-12d3-a456-426614174000",
                                "workspace_id": 12345,
                                "status": "approved",
                                "data": {
                                  "end_of_week": 1672531199000,
                                  "start_of_week": 1671926400000
                                },
                                "user": {
                                  "id": 101,
                                  "username": "john.smith",
                                  "initials": "JS",
                                  "avatar": {
                                    "color": "#4287f5",
                                    "picture_url": null
                                  }
                                },
                                "approvers": [
                                  {
                                    "id": 101
                                  },
                                  {
                                    "id": 102
                                  }
                                ],
                                "approver_id": 101,
                                "approved_at": 1672012800000,
                                "history": [
                                  {
                                    "id": "987fcdeb-51a2-3456-789a-bcdef0123456",
                                    "field": "submission",
                                    "before": null,
                                    "after": null,
                                    "created_at": 1671987600000,
                                    "user": {
                                      "id": 101,
                                      "username": "john.smith",
                                      "role": "submitter"
                                    }
                                  },
                                  {
                                    "id": "456abcde-f123-4567-89ab-cdef01234567",
                                    "field": "status",
                                    "before": "pending",
                                    "after": "approved",
                                    "created_at": 1672012800000,
                                    "user": {
                                      "id": 102,
                                      "username": "jane.doe",
                                      "role": "approver"
                                    }
                                  }
                                ]
                              }
                            ]
                          },
                          "task_location": {
                            "list_id": 1560300071,
                            "folder_id": 468300080,
                            "space_id": 22800253,
                            "list_name": "List",
                            "folder_name": "Folder",
                            "space_name": "Space"
                          },
                          "task_tags": [
                            {
                              "name": "content-request",
                              "tag_fg": "#800000",
                              "tag_bg": "#2ecd6f",
                              "creator": 301828
                            },
                            {
                              "name": "marketing-okr",
                              "tag_fg": "#800000",
                              "tag_bg": "#7C4DFF",
                              "creator": 301828
                            }
                          ],
                          "task_url": "https://staging.clickup.com/t/rnmuwz7"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "data": [
                        {
                          "id": "timer_id",
                          "wid": "workspace_id",
                          "user": {
                            "id": 1,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": "1592841559129",
                          "end": "1592845899021",
                          "duration": "4339892",
                          "description": "",
                          "tags": [],
                          "source": "clickup",
                          "at": "1592845899021",
                          "approval_id": "2d539936-119a-4927-9770-179f0a72e2e5",
                          "approval": {
                            "title": "Approval",
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "Unique identifier for the approval"
                              },
                              "workspace_id": {
                                "type": "integer",
                                "description": "ID of the workspace this approval belongs to"
                              },
                              "status": {
                                "type": "string",
                                "description": "Current status of the approval (e.g., 'approved', 'pending')"
                              },
                              "data": {
                                "type": "object",
                                "properties": {
                                  "end_of_week": {
                                    "type": "integer",
                                    "description": "Timestamp for the end of the week"
                                  },
                                  "start_of_week": {
                                    "type": "integer",
                                    "description": "Timestamp for the start of the week"
                                  }
                                }
                              },
                              "user": {
                                "title": "User13",
                                "required": [
                                  "id",
                                  "username",
                                  "email",
                                  "color",
                                  "initials",
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
                                  "email": {
                                    "type": "string"
                                  },
                                  "color": {
                                    "type": "string"
                                  },
                                  "initials": {
                                    "type": "string"
                                  },
                                  "profilePicture": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  }
                                },
                                "examples": [
                                  {
                                    "id": 1,
                                    "username": "John Doe",
                                    "email": "johndoe@gmail.com",
                                    "color": "#795548",
                                    "initials": "JD",
                                    "profilePicture": null
                                  }
                                ]
                              },
                              "approvers": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer",
                                      "description": "ID of the user who can approve the request"
                                    }
                                  }
                                }
                              },
                              "approver_id": {
                                "type": "integer",
                                "description": "ID of the user who approved the request"
                              },
                              "approved_at": {
                                "type": "integer",
                                "description": "Timestamp when the approval was granted"
                              },
                              "history": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "string",
                                      "description": "Unique identifier for the history entry"
                                    },
                                    "field": {
                                      "type": "string",
                                      "description": "Field that was changed"
                                    },
                                    "before": {
                                      "type": "string",
                                      "description": "Previous value"
                                    },
                                    "after": {
                                      "type": "string",
                                      "description": "New value"
                                    },
                                    "created_at": {
                                      "type": "integer",
                                      "description": "Timestamp when the change was made"
                                    },
                                    "user": {
                                      "title": "User13",
                                      "required": [
                                        "id",
                                        "username",
                                        "email",
                                        "color",
                                        "initials",
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
                                        "email": {
                                          "type": "string"
                                        },
                                        "color": {
                                          "type": "string"
                                        },
                                        "initials": {
                                          "type": "string"
                                        },
                                        "profilePicture": {
                                          "type": [
                                            "string",
                                            "null"
                                          ]
                                        }
                                      },
                                      "examples": [
                                        {
                                          "id": 1,
                                          "username": "John Doe",
                                          "email": "johndoe@gmail.com",
                                          "color": "#795548",
                                          "initials": "JD",
                                          "profilePicture": null
                                        }
                                      ]
                                    }
                                  }
                                }
                              }
                            },
                            "examples": [
                              {
                                "id": "123e4567-e89b-12d3-a456-426614174000",
                                "workspace_id": 12345,
                                "status": "approved",
                                "data": {
                                  "end_of_week": 1672531199000,
                                  "start_of_week": 1671926400000
                                },
                                "user": {
                                  "id": 101,
                                  "username": "john.smith",
                                  "initials": "JS",
                                  "avatar": {
                                    "color": "#4287f5",
                                    "picture_url": null
                                  }
                                },
                                "approvers": [
                                  {
                                    "id": 101
                                  },
                                  {
                                    "id": 102
                                  }
                                ],
                                "approver_id": 101,
                                "approved_at": 1672012800000,
                                "history": [
                                  {
                                    "id": "987fcdeb-51a2-3456-789a-bcdef0123456",
                                    "field": "submission",
                                    "before": null,
                                    "after": null,
                                    "created_at": 1671987600000,
                                    "user": {
                                      "id": 101,
                                      "username": "john.smith",
                                      "role": "submitter"
                                    }
                                  },
                                  {
                                    "id": "456abcde-f123-4567-89ab-cdef01234567",
                                    "field": "status",
                                    "before": "pending",
                                    "after": "approved",
                                    "created_at": 1672012800000,
                                    "user": {
                                      "id": 102,
                                      "username": "jane.doe",
                                      "role": "approver"
                                    }
                                  }
                                ]
                              }
                            ]
                          },
                          "task_location": {
                            "list_id": 1560300071,
                            "folder_id": 468300080,
                            "space_id": 22800253,
                            "list_name": "List",
                            "folder_name": "Folder",
                            "space_name": "Space"
                          },
                          "task_tags": [
                            {
                              "name": "content-request",
                              "tag_fg": "#800000",
                              "tag_bg": "#2ecd6f",
                              "creator": 301828
                            },
                            {
                              "name": "marketing-okr",
                              "tag_fg": "#800000",
                              "tag_bg": "#7C4DFF",
                              "creator": 301828
                            }
                          ],
                          "task_url": "https://staging.clickup.com/t/rnmuwz7"
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "data": [
                    {
                      "id": "timer_id",
                      "wid": "workspace_id",
                      "user": {
                        "id": 1,
                        "username": "first_name last_name",
                        "email": "test@gmail.com",
                        "color": "#08c7e0",
                        "initials": "JK",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                      },
                      "billable": false,
                      "start": "1592841559129",
                      "end": "1592845899021",
                      "duration": "4339892",
                      "description": "",
                      "source": "clickup",
                      "at": "1592845899021",
                      "task_location": {
                        "list_id": 1560300071,
                        "folder_id": 468300080,
                        "space_id": 22800253,
                        "list_name": "List",
                        "folder_name": "Folder",
                        "space_name": "Space"
                      },
                      "task_tags": [
                        {
                          "name": "content-request",
                          "tag_fg": "#800000",
                          "tag_bg": "#2ecd6f",
                          "creator": 301828
                        },
                        {
                          "name": "marketing-okr",
                          "tag_fg": "#800000",
                          "tag_bg": "#7C4DFF",
                          "creator": 301828
                        }
                      ],
                      "task_url": "https://staging.clickup.com/t/rnmuwz7"
                    }
                  ]
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
      "name": "Time Tracking"
    }
  ]
}
```