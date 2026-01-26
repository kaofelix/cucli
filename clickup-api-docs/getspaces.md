# Get Spaces

View the Spaces avialable in a Workspace. You can only get member info in private Spaces.

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
    "/v2/team/{team_id}/space": {
      "get": {
        "summary": "Get Spaces",
        "tags": [
          "Spaces"
        ],
        "description": "View the Spaces avialable in a Workspace. You can only get member info in private Spaces.",
        "operationId": "GetSpaces",
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
            "name": "archived",
            "in": "query",
            "description": "",
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
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetSpacesresponse",
                  "required": [
                    "spaces"
                  ],
                  "type": "object",
                  "properties": {
                    "spaces": {
                      "type": "array",
                      "items": {
                        "title": "Space13",
                        "required": [
                          "id",
                          "name",
                          "private",
                          "statuses",
                          "multiple_assignees",
                          "features"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "private": {
                            "type": "boolean"
                          },
                          "color": {
                            "type": "string"
                          },
                          "avatar": {
                            "type": "string"
                          },
                          "admin_can_manage": {
                            "type": "boolean"
                          },
                          "archived": {
                            "type": "boolean"
                          },
                          "members": {
                            "type": "array",
                            "items": {
                              "title": "Member",
                              "required": [
                                "user"
                              ],
                              "type": "object",
                              "properties": {
                                "user": {
                                  "title": "User",
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
                                    "profilePicture": {
                                      "type": "string"
                                    },
                                    "initials": {
                                      "type": "string"
                                    },
                                    "week_start_day": {
                                      "type": "integer",
                                      "contentEncoding": "int32",
                                      "description": "The user's preferred start of the calendar week setting. \\ `0` is Sunday. \\ `1` is Monday."
                                    },
                                    "global_font_support": {
                                      "type": "boolean"
                                    },
                                    "timezeone": {
                                      "type": "string"
                                    }
                                  },
                                  "examples": [
                                    {
                                      "id": 123,
                                      "username": "John Doe",
                                      "email": "user@company.com",
                                      "color": "#000000",
                                      "profilePicture": "https://clickup.com/avatar.jpg",
                                      "initials": "JD",
                                      "week_start_day": 0,
                                      "global_font_support": false,
                                      "timezone": "America/Los_Angeles"
                                    }
                                  ]
                                }
                              },
                              "examples": [
                                {
                                  "user": {
                                    "id": 123,
                                    "username": "John Doe",
                                    "color": "#000000",
                                    "profilePicture": "https://clickup.com/avatar.jpg"
                                  }
                                }
                              ]
                            },
                            "description": "",
                            "user": {
                              "id": {
                                "type": "string"
                              },
                              "username": {
                                "type": "string"
                              },
                              "color": {
                                "type": "string"
                              },
                              "profilePicture": {
                                "type": "string"
                              },
                              "initials": {
                                "type": "string"
                              }
                            }
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
                          "multiple_assignees": {
                            "type": "boolean"
                          },
                          "features": {
                            "title": "Features4",
                            "required": [
                              "due_dates",
                              "time_tracking",
                              "tags",
                              "time_estimates",
                              "checklists"
                            ],
                            "type": "object",
                            "properties": {
                              "due_dates": {
                                "title": "DueDates",
                                "required": [
                                  "enabled",
                                  "start_date",
                                  "remap_due_dates",
                                  "remap_closed_due_date"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  },
                                  "start_date": {
                                    "type": "boolean"
                                  },
                                  "remap_due_dates": {
                                    "type": "boolean"
                                  },
                                  "remap_closed_due_date": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true,
                                    "start_date": false,
                                    "remap_due_dates": true,
                                    "remap_closed_due_date": false
                                  }
                                ]
                              },
                              "time_tracking": {
                                "title": "TimeTracking",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": false
                                  }
                                ]
                              },
                              "tags": {
                                "title": "Tags",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              },
                              "time_estimates": {
                                "title": "TimeEstimates",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              },
                              "checklists": {
                                "title": "Checklists",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              },
                              "custom_fields": {
                                "title": "CustomFields",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              },
                              "remap_dependencies": {
                                "title": "RemapDependencies",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              },
                              "dependency_warning": {
                                "title": "DependencyWarning",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              },
                              "portfolios": {
                                "title": "Portfolios",
                                "required": [
                                  "enabled"
                                ],
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "enabled": true
                                  }
                                ]
                              }
                            },
                            "examples": [
                              {
                                "due_dates": {
                                  "enabled": false,
                                  "start_date": false,
                                  "remap_due_dates": false,
                                  "remap_closed_due_date": false
                                },
                                "time_tracking": {
                                  "enabled": false
                                },
                                "tags": {
                                  "enabled": false
                                },
                                "time_estimates": {
                                  "enabled": false
                                },
                                "checklists": {
                                  "enabled": true
                                },
                                "custom_fields": {
                                  "enabled": true
                                },
                                "remap_dependencies": {
                                  "enabled": false
                                },
                                "dependency_warning": {
                                  "enabled": false
                                },
                                "portfolios": {
                                  "enabled": false
                                }
                              }
                            ]
                          }
                        },
                        "examples": [
                          {
                            "id": "790",
                            "name": "Updated Space Name",
                            "private": false,
                            "color": null,
                            "avatar": "https://attachments.clickup.com/profilePictures/12312312_HoB.jpg",
                            "admin_can_manage": true,
                            "archived": false,
                            "members": [
                              {
                                "user": {
                                  "id": 12312312,
                                  "username": "John Jones",
                                  "color": null,
                                  "profilePicture": "https://attachments.clickup.com/profilePictures/12312312_HoB.jpg",
                                  "initials": "JJ"
                                }
                              }
                            ],
                            "statuses": [
                              {
                                "status": "to do",
                                "type": "open",
                                "orderindex": 0,
                                "color": "#d3d3d3"
                              },
                              {
                                "status": "complete",
                                "type": "closed",
                                "orderindex": 1,
                                "color": "#6bc950"
                              }
                            ],
                            "multiple_assignees": false,
                            "features": {
                              "due_dates": {
                                "enabled": false,
                                "start_date": false,
                                "remap_due_dates": false,
                                "remap_closed_due_date": false
                              },
                              "time_tracking": {
                                "enabled": false
                              },
                              "tags": {
                                "enabled": false
                              },
                              "time_estimates": {
                                "enabled": false
                              },
                              "checklists": {
                                "enabled": true
                              },
                              "custom_fields": {
                                "enabled": true
                              },
                              "remap_dependencies": {
                                "enabled": false
                              },
                              "dependency_warning": {
                                "enabled": false
                              },
                              "portfolios": {
                                "enabled": false
                              }
                            }
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "spaces": [
                        {
                          "id": "790",
                          "name": "Updated Space Name",
                          "private": false,
                          "color": null,
                          "avatar": "https://attachments.clickup.com/profilePictures/12312312_HoB.jpg",
                          "admin_can_manage": true,
                          "archived": false,
                          "members": [
                            {
                              "user": {
                                "id": "12312312,",
                                "username": "John Jones,",
                                "color": null,
                                "profilePicture": "https://attachments.clickup.com/profilePictures/12312312_HoB.jpg,",
                                "initials": "JJ"
                              }
                            }
                          ],
                          "statuses": [
                            {
                              "status": "to do",
                              "type": "open",
                              "orderindex": 0,
                              "color": "#d3d3d3"
                            },
                            {
                              "status": "complete",
                              "type": "closed",
                              "orderindex": 1,
                              "color": "#6bc950"
                            }
                          ],
                          "multiple_assignees": false,
                          "features": {
                            "due_dates": {
                              "enabled": false,
                              "start_date": false,
                              "remap_due_dates": false,
                              "remap_closed_due_date": false
                            },
                            "time_tracking": {
                              "enabled": false
                            },
                            "tags": {
                              "enabled": false
                            },
                            "time_estimates": {
                              "enabled": false
                            },
                            "checklists": {
                              "enabled": true
                            },
                            "custom_fields": {
                              "enabled": true
                            },
                            "remap_dependencies": {
                              "enabled": false
                            },
                            "dependency_warning": {
                              "enabled": false
                            },
                            "portfolios": {
                              "enabled": false
                            }
                          }
                        },
                        {
                          "id": "791",
                          "name": "Second Space Name",
                          "private": false,
                          "statuses": [
                            {
                              "status": "Open",
                              "type": "open",
                              "orderindex": 0,
                              "color": "#d3d3d3"
                            },
                            {
                              "status": "Closed",
                              "type": "closed",
                              "orderindex": 1,
                              "color": "#6bc950"
                            }
                          ],
                          "multiple_assignees": true,
                          "features": {
                            "due_dates": {
                              "enabled": true,
                              "start_date": false,
                              "remap_due_dates": false,
                              "remap_closed_due_date": false
                            },
                            "time_tracking": {
                              "enabled": true
                            },
                            "tags": {
                              "enabled": true
                            },
                            "time_estimates": {
                              "enabled": true
                            },
                            "checklists": {
                              "enabled": true
                            }
                          }
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "spaces": [
                    {
                      "id": "790",
                      "name": "Updated Space Name",
                      "private": false,
                      "color": null,
                      "avatar": "https://attachments.clickup.com/profilePictures/12312312_HoB.jpg",
                      "admin_can_manage": true,
                      "archived": false,
                      "members": [
                        {
                          "user": {
                            "id": "12312312,",
                            "username": "John Jones,",
                            "color": null,
                            "profilePicture": "https://attachments.clickup.com/profilePictures/12312312_HoB.jpg,",
                            "initials": "JJ"
                          }
                        }
                      ],
                      "statuses": [
                        {
                          "status": "to do",
                          "type": "open",
                          "orderindex": 0,
                          "color": "#d3d3d3"
                        },
                        {
                          "status": "complete",
                          "type": "closed",
                          "orderindex": 1,
                          "color": "#6bc950"
                        }
                      ],
                      "multiple_assignees": false,
                      "features": {
                        "due_dates": {
                          "enabled": false,
                          "start_date": false,
                          "remap_due_dates": false,
                          "remap_closed_due_date": false
                        },
                        "time_tracking": {
                          "enabled": false
                        },
                        "tags": {
                          "enabled": false
                        },
                        "time_estimates": {
                          "enabled": false
                        },
                        "checklists": {
                          "enabled": true
                        },
                        "custom_fields": {
                          "enabled": true
                        },
                        "remap_dependencies": {
                          "enabled": false
                        },
                        "dependency_warning": {
                          "enabled": false
                        },
                        "portfolios": {
                          "enabled": false
                        }
                      }
                    },
                    {
                      "id": "791",
                      "name": "Second Space Name",
                      "private": false,
                      "statuses": [
                        {
                          "status": "Open",
                          "type": "open",
                          "orderindex": 0,
                          "color": "#d3d3d3"
                        },
                        {
                          "status": "Closed",
                          "type": "closed",
                          "orderindex": 1,
                          "color": "#6bc950"
                        }
                      ],
                      "multiple_assignees": true,
                      "features": {
                        "due_dates": {
                          "enabled": true,
                          "start_date": false,
                          "remap_due_dates": false,
                          "remap_closed_due_date": false
                        },
                        "time_tracking": {
                          "enabled": true
                        },
                        "tags": {
                          "enabled": true
                        },
                        "time_estimates": {
                          "enabled": true
                        },
                        "checklists": {
                          "enabled": true
                        }
                      }
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
      "name": "Spaces"
    }
  ]
}
```