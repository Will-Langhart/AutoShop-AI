autoshop-ai/
│── backend/                              # Flask backend
│   │── app.py                            # Main application file
│   │── models.py                         # Database models
│   │── routes/                           # API routes
│   │   │── store.py                       # Store generation logic
│   │   │── marketing.py                    # Automated marketing APIs
│   │── services/                          # Business logic
│   │   │── gpt4_service.py                 # AI product descriptions
│   │   │── image_generator.py              # Stable Diffusion AI image gen
│   │── config.py                          # Configuration settings
│   │── database.py                        # Database setup (PostgreSQL)
│   │── requirements.txt                   # Dependencies
│   └── tests/                             # Unit tests
│
│── frontend/                             # Next.js/React frontend
│   │── pages/                            # UI pages
│   │   │── index.js                       # Home page
│   │   │── store-builder.js               # Store customization page
│   │── components/                        # UI Components
│   │   │── ProductForm.js                  # Product addition form
│   │   │── StorePreview.js                 # Preview of generated store
│   │── styles/                            # Tailwind CSS styles
│   │── package.json                       # Frontend dependencies
│   └── tests/                             # Unit tests for frontend
│
│── docs/                                 # Documentation
│── README.md                             # Project overview
└── Dockerfile                            # Containerization setup
