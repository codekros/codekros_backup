<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Stock Expiry List - Updated Design</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <!-- Bootstrap 5 via CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
  
  <style>
    .expiry-badge {
      font-size: 0.8rem;
      padding: 0.25rem 0.5rem;
    }
    .expiry-weekly {
      background-color: #e3f2fd;
      color: #1976d2;
    }
    .expiry-monthly {
      background-color: #f3e5f5;
      color: #7b1fa2;
    }
    .table-hover tbody tr:hover {
      background-color: rgba(0,123,255,0.1);
    }
    .search-box {
      max-width: 300px;
    }
    .filter-buttons .btn {
      margin-right: 0.5rem;
      margin-bottom: 0.5rem;
    }
  </style>
</head>
<body class="bg-light">
  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="/">
        <i class="bi bi-graph-up"></i> ALGOTRADING
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-briefcase"></i> Open Positions</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-pie-chart"></i> Portfolio</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-calendar-plus"></i> Add Expiry</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#"><i class="bi bi-calendar-check"></i> Stock Expiry</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-building"></i> Add Stock</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-graph-up"></i> Option Chain</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-bar-chart"></i> Analysis</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="bi bi-box-arrow-right"></i> Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Main Content -->
  <div class="container mt-4">
    <!-- Header Section -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="card shadow-sm">
          <div class="card-body">
            <div class="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h4 class="mb-1"><i class="bi bi-calendar-check text-primary"></i> Stock Expiry Management</h4>
                <p class="text-muted mb-0">Manage expiry dates for trading instruments</p>
              </div>
              <div class="d-flex gap-2">
                <button class="btn btn-success">
                  <i class="bi bi-plus-circle"></i> Add New Expiry
                </button>
                <button class="btn btn-info">
                  <i class="bi bi-calendar-week"></i> Add Weekly Expiry
                </button>
              </div>
            </div>

            <!-- Search and Filter Section -->
            <div class="row">
              <div class="col-md-6">
                <div class="input-group search-box">
                  <span class="input-group-text"><i class="bi bi-search"></i></span>
                  <input type="text" class="form-control" placeholder="Search by expiry date or type...">
                </div>
              </div>
              <div class="col-md-6">
                <div class="filter-buttons">
                  <button class="btn btn-outline-primary btn-sm active">All</button>
                  <button class="btn btn-outline-primary btn-sm">Weekly</button>
                  <button class="btn btn-outline-primary btn-sm">Monthly</button>
                  <button class="btn btn-outline-secondary btn-sm">
                    <i class="bi bi-funnel"></i> More Filters
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Data Table Section -->
    <div class="row">
      <div class="col-12">
        <div class="card shadow-sm">
          <div class="card-body">
            <!-- Table Header with Stats -->
            <div class="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h6 class="mb-0">Expiry Records</h6>
                <small class="text-muted">Showing 8 of 8 records</small>
              </div>
              <div class="d-flex gap-2">
                <button class="btn btn-outline-secondary btn-sm">
                  <i class="bi bi-download"></i> Export
                </button>
                <button class="btn btn-outline-secondary btn-sm">
                  <i class="bi bi-arrow-clockwise"></i> Refresh
                </button>
              </div>
            </div>

            <!-- Data Table -->
            <div class="table-responsive">
              <table class="table table-hover">
                <thead class="table-dark">
                  <tr>
                    <th>
                      <input type="checkbox" class="form-check-input">
                    </th>
                    <th>Expiry ID</th>
                    <th>Expiry Type</th>
                    <th>Expiry Date</th>
                    <th>Days Until Expiry</th>
                    <th>Created Date</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <!-- Sample Data Row 1 -->
                  <tr>
                    <td>
                      <input type="checkbox" class="form-check-input">
                    </td>
                    <td>
                      <span class="fw-bold text-primary">#001</span>
                    </td>
                    <td>
                      <span class="badge expiry-badge expiry-weekly">
                        <i class="bi bi-calendar-week"></i> Weekly
                      </span>
                    </td>
                    <td>
                      <span class="fw-bold">Jan 15, 2025</span>
                    </td>
                    <td>
                      <span class="badge bg-warning text-dark">12 days</span>
                    </td>
                    <td>
                      <small class="text-muted">Dec 20, 2024</small>
                    </td>
                    <td>
                      <span class="badge bg-success">Active</span>
                    </td>
                    <td>
                      <div class="btn-group btn-group-sm">
                        <button class="btn btn-outline-primary" title="Edit">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-outline-info" title="View Details">
                          <i class="bi bi-eye"></i>
                        </button>
                        <button class="btn btn-outline-danger" title="Delete">
                          <i class="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>

                  <!-- Sample Data Row 2 -->
                  <tr>
                    <td>
                      <input type="checkbox" class="form-check-input">
                    </td>
                    <td>
                      <span class="fw-bold text-primary">#002</span>
                    </td>
                    <td>
                      <span class="badge expiry-badge expiry-monthly">
                        <i class="bi bi-calendar-month"></i> Monthly
                      </span>
                    </td>
                    <td>
                      <span class="fw-bold">Jan 30, 2025</span>
                    </td>
                    <td>
                      <span class="badge bg-info text-white">27 days</span>
                    </td>
                    <td>
                      <small class="text-muted">Dec 18, 2024</small>
                    </td>
                    <td>
                      <span class="badge bg-success">Active</span>
                    </td>
                    <td>
                      <div class="btn-group btn-group-sm">
                        <button class="btn btn-outline-primary" title="Edit">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-outline-info" title="View Details">
                          <i class="bi bi-eye"></i>
                        </button>
                        <button class="btn btn-outline-danger" title="Delete">
                          <i class="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>

                  <!-- Sample Data Row 3 -->
                  <tr>
                    <td>
                      <input type="checkbox" class="form-check-input">
                    </td>
                    <td>
                      <span class="fw-bold text-primary">#003</span>
                    </td>
                    <td>
                      <span class="badge expiry-badge expiry-weekly">
                        <i class="bi bi-calendar-week"></i> Weekly
                      </span>
                    </td>
                    <td>
                      <span class="fw-bold">Feb 06, 2025</span>
                    </td>
                    <td>
                      <span class="badge bg-primary text-white">34 days</span>
                    </td>
                    <td>
                      <small class="text-muted">Dec 15, 2024</small>
                    </td>
                    <td>
                      <span class="badge bg-success">Active</span>
                    </td>
                    <td>
                      <div class="btn-group btn-group-sm">
                        <button class="btn btn-outline-primary" title="Edit">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-outline-info" title="View Details">
                          <i class="bi bi-eye"></i>
                        </button>
                        <button class="btn btn-outline-danger" title="Delete">
                          <i class="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>

                  <!-- Sample Data Row 4 -->
                  <tr>
                    <td>
                      <input type="checkbox" class="form-check-input">
                    </td>
                    <td>
                      <span class="fw-bold text-primary">#004</span>
                    </td>
                    <td>
                      <span class="badge expiry-badge expiry-monthly">
                        <i class="bi bi-calendar-month"></i> Monthly
                      </span>
                    </td>
                    <td>
                      <span class="fw-bold">Feb 27, 2025</span>
                    </td>
                    <td>
                      <span class="badge bg-secondary text-white">55 days</span>
                    </td>
                    <td>
                      <small class="text-muted">Dec 10, 2024</small>
                    </td>
                    <td>
                      <span class="badge bg-warning text-dark">Pending</span>
                    </td>
                    <td>
                      <div class="btn-group btn-group-sm">
                        <button class="btn btn-outline-primary" title="Edit">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-outline-info" title="View Details">
                          <i class="bi bi-eye"></i>
                        </button>
                        <button class="btn btn-outline-danger" title="Delete">
                          <i class="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Pagination -->
            <div class="d-flex justify-content-between align-items-center mt-3">
              <div>
                <small class="text-muted">Showing 1 to 4 of 4 entries</small>
              </div>
              <nav>
                <ul class="pagination pagination-sm mb-0">
                  <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">Previous</a>
                  </li>
                  <li class="page-item active">
                    <a class="page-link" href="#">1</a>
                  </li>
                  <li class="page-item disabled">
                    <a class="page-link" href="#">Next</a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Summary Cards -->
    <div class="row mt-4">
      <div class="col-md-3">
        <div class="card bg-primary text-white">
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <div>
                <h6 class="card-title">Total Expiries</h6>
                <h4 class="mb-0">24</h4>
              </div>
              <div class="align-self-center">
                <i class="bi bi-calendar-check fs-1"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card bg-success text-white">
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <div>
                <h6 class="card-title">Weekly Expiries</h6>
                <h4 class="mb-0">16</h4>
              </div>
              <div class="align-self-center">
                <i class="bi bi-calendar-week fs-1"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card bg-info text-white">
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <div>
                <h6 class="card-title">Monthly Expiries</h6>
                <h4 class="mb-0">8</h4>
              </div>
              <div class="align-self-center">
                <i class="bi bi-calendar-month fs-1"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card bg-warning text-dark">
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <div>
                <h6 class="card-title">Upcoming (7 days)</h6>
                <h4 class="mb-0">3</h4>
              </div>
              <div class="align-self-center">
                <i class="bi bi-clock fs-1"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  
  <!-- Sample JavaScript for interactivity -->
  <script>
    // Sample JavaScript for search and filter functionality
    document.addEventListener('DOMContentLoaded', function() {
      // Search functionality
      const searchInput = document.querySelector('input[type="text"]');
      searchInput.addEventListener('input', function() {
        console.log('Searching for:', this.value);
        // Add search logic here
      });

      // Filter buttons
      const filterButtons = document.querySelectorAll('.filter-buttons .btn');
      filterButtons.forEach(button => {
        button.addEventListener('click', function() {
          // Remove active class from all buttons
          filterButtons.forEach(btn => btn.classList.remove('active'));
          // Add active class to clicked button
          this.classList.add('active');
          console.log('Filter applied:', this.textContent.trim());
        });
      });

      // Checkbox functionality
      const checkboxes = document.querySelectorAll('input[type="checkbox"]');
      checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
          console.log('Checkbox changed:', this.checked);
        });
      });
    });
  </script>
</body>
</html>
