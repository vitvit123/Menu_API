<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }

        .profile-container {
            max-width: 600px;
            margin: 80px auto;
            background-color: #ffffff;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            display: flex;
        }

        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            margin-right: 30px;
            border: 5px solid #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .profile-info {
            flex: 1;
        }

        .profile-name {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .profile-email {
            font-size: 18px;
            color: #6c757d;
            margin-bottom: 20px;
        }

        .profile-actions {
            text-align: center;
        }

        .btn-change-profile {
            width: 100%;
            margin-bottom: 10px;
        }

        .btn-change-profile:hover {
            background-color: #007bff;
            border-color: #007bff;
        }

        .btn-change-profile:focus {
            box-shadow: 0 0 0 0.25rem rgba(38, 143, 255, 0.5);
        }

        .modal-dialog {
            max-width: 400px;
        }

        .modal-content {
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
        }

        .modal-title {
            font-size: 24px;
            font-weight: bold;
            color: #343a40;
            margin-bottom: 15px;
        }

        #newProfileImg {
            margin-bottom: 15px;
        }

        .profile-info {
            margin-bottom: 20px;
        }

        .profile-info h3 {
            font-size: 20px;
            color: #343a40;
            margin-bottom: 10px;
        }

        .profile-info p {
            color: #6c757d;
            margin-bottom: 0;
        }

        .logout-link {
            color: #dc3545;
        }

        .logout-link:hover {
            color: #bd2130;
        }
    </style>
</head>
<body>

<div class="container profile-container">
    <div class="profile-img-container">
        <img src="images/profile/0a3899c4ff6ccca2e7152085fdfc2ab9.jpg" alt="Profile Picture" class="profile-img">
    </div>

    <div class="profile-info">
        <div class="profile-name">John Doe</div>
        <div class="profile-email">johndoe@example.com</div>

        <div class="profile-actions">
            <a href="#" class="btn btn-primary btn-change-profile" data-bs-toggle="modal" data-bs-target="#changeProfileModal">Change Profile Picture</a>
            <a href="#" class="btn btn-outline-danger logout-link">Logout</a>
        </div>
    </div>
</div>

<!-- Change Profile Picture Modal -->
<div class="modal fade" id="changeProfileModal" tabindex="-1" aria-labelledby="changeProfileModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="changeProfileModalLabel">Change Profile Picture</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="profileForm">
                    <div class="mb-3">
                        <label for="newProfileImg" class="form-label">Choose new profile picture:</label>
                        <input type="file" class="form-control" id="newProfileImg" accept="image/*">
                    </div>
                    <button type="submit" class="btn btn-primary">Upload</button>
                </form>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
