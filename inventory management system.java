import java.sql.*;
import java.util.Scanner;

public class inventory2{

    static final String URL = "jdbc:mysql://localhost:3306/inventory_db";
    static final String USER = "root";  // Change as per your DB
    static final String PASSWORD = ""; // Change as per your DB

    static Scanner scanner = new Scanner(System.in);
    static Connection conn;

    public static void main(String[] args) {
        try {
            // Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish connection
            conn = DriverManager.getConnection(URL, USER, PASSWORD);
            System.out.println("Connected to Inventory Database!");

            System.out.print("Enter Username: ");
            String username = scanner.nextLine();
            System.out.print("Enter Password: ");
            String password = scanner.nextLine();

            String role = authenticateUser(username, password);

            if (role == null) {
                System.out.println("Invalid credentials! Exiting...");
                return;
            }

            System.out.println("Logged in as: " + role);
            showMenu(role);

        } catch (SQLException e) {
            System.err.println("Database Error: " + e.getMessage());
        } catch (ClassNotFoundException e) {

            System.err.println("JDBC Driver Not Found! Ensure mysql-connector-java.jar is in the classpath.");
        } finally {
            closeConnection();
        }
    }

    public static String authenticateUser(String username, String password) throws SQLException {
        String query = "SELECT role FROM users WHERE username=? AND password=?";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, username);
        stmt.setString(2, password);
        ResultSet rs = stmt.executeQuery();
        return rs.next() ? rs.getString("role") : null;
    }

    public static void showMenu(String role) throws SQLException {
        while (true) {
            System.out.println("\n===== INVENTORY MANAGEMENT =====");

            if (role.equals("admin")) {
                System.out.println("1. View Products");
                System.out.println("2. Add Product");
                System.out.println("3. Update Product");
                System.out.println("4. Delete Product");
                System.out.println("5. Stock In");
                System.out.println("6. Stock Out");
                System.out.println("7. Manage Suppliers");
                System.out.println("8. Manage Customers");
                System.out.println("9. Manage Users (only for admin)");
                System.out.println("10. exit");
            } else if (role.equals("staff")) {
                System.out.println("1. View Products");
                System.out.println("5. Stock In");
                System.out.println("6. Stock Out");
                System.out.println("7. Manage Suppliers");
                System.out.println("8. Manage Customers");
                System.out.println("10. exit");

            } else if (role.equals("manager")) {
                System.out.println("1. View Products");
                System.out.println("2. Add Product");
                System.out.println("3. Update Product");
                System.out.println("4. Delete Product");
                System.out.println("5. Stock In");
                System.out.println("6. Stock Out");
                System.out.println("7. Manage Suppliers");
                System.out.println("8. Manage Customers");
                System.out.println("10. exit");
            }

            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    viewProducts();
                    break;
                case 2: {
                    if (!role.equals("staff")) {
                        addProduct();
                        break;

                    } else {
                        System.out.println("Invalid choice!");
                    }
                    break;
                }
                case 3: {
                    if (!role.equals("staff")) {
                        updateProduct();
                        break;
                    } else {
                        System.out.println("Invalid choice!");

                    }
                    break;
                }
                case 4: {
                    if (!role.equals("staff")) {
                        deleteProduct();

                    } else {
                        System.out.println("Invalid choice!");
                    }

                    break;
                }
                case 5:
                    stockIn();
                    break;
                case 6:
                    stockOut();
                    break;
                case 7:
                    manageSuppliers();
                    break;

                case 8:
                    manageCustomers();
                    break;
                case 9: {
                    if (role.equals("admin")) {
                        manageUsers();
                        break;
                    } else {
                        System.out.println("Invalid choice!");
                        break;
                    }
                }
                case 10: {
                    System.out.println("Exiting...");
                    return;
                }
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }

    public static void manageUsers() throws SQLException {
        while (true) {
            System.out.println("\n===== USER MANAGEMENT =====");
            System.out.println("1. View Users");
            System.out.println("2. Add User");
            System.out.println("3. Delete User");
            System.out.println("4. Back to Main Menu");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    viewUsers();
                    break;
                case 2:
                    addUser();
                    break;
                case 3:
                    deleteUser();
                    break;
                case 4: {
                    return;
                }
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }

    public static void viewUsers() throws SQLException {
        String query = "SELECT id, username, role FROM users";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);

        System.out.println("\nID | Username | Role");
        System.out.println("------------------------");
        while (rs.next()) {
            System.out.println(rs.getInt("id") + " | " + rs.getString("username") + " | " + rs.getString("role"));
        }
    }

    public static void addUser() throws SQLException {
        System.out.print("Enter New Username: ");
        String username = scanner.nextLine();
        System.out.print("Enter Password: ");
        String password = scanner.nextLine();
        System.out.print("Enter Role (manager/staff): ");
        String role = scanner.nextLine().toLowerCase();

        if (!role.equals("manager") && !role.equals("staff")) {
            System.out.println("Invalid role! Only 'manager' or 'staff' are allowed.");
            return;
        }

        String query = "INSERT INTO users (username, password, role) VALUES (?, ?, ?)";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, username);
        stmt.setString(2, password);
        stmt.setString(3, role);
        stmt.executeUpdate();
        System.out.println("User added successfully!");
    }

    public static void deleteUser() throws SQLException {
        System.out.print("Enter User ID to delete: ");
        int id = scanner.nextInt();
        scanner.nextLine();
        String checkQuery = "SELECT COUNT(*) FROM users WHERE id = ?";
        try (PreparedStatement checkStmt = conn.prepareStatement(checkQuery)) {
            checkStmt.setInt(1, id);
            try (ResultSet rs = checkStmt.executeQuery()) {
                rs.next();
                int count = rs.getInt(1);
                if (count == 0) {
                    System.out.println("Please enter a valid user ID");
                    return;
                }
            }
        } catch (SQLException e) {
            System.out.println("Error checking customer ID: " + e.getMessage());
            throw e;
        }
        String query = "DELETE FROM users WHERE id=?";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setInt(1, id);
        stmt.executeUpdate();
        System.out.println("User deleted successfully!");
    }

    public static void viewProducts() throws SQLException {
        String query = "SELECT * FROM products";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);

        System.out.println("\nID   | Name             | Category       | Quantity   | Price");
        System.out.println("-----------------------------------------------------------------");
        while (rs.next()) {
            System.out.printf("%-4d | %-15s | %-15s | %-10d | %.2f%n",
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("category"),
                    rs.getInt("quantity"),
                    rs.getDouble("price")
            );

        }
    }

    public static void addProduct() throws SQLException {
        System.out.print("Enter Product Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Category: ");
        String category = scanner.nextLine();
        System.out.print("Enter Quantity: ");
        int quantity = scanner.nextInt();
        System.out.print("Enter Price: ");
        double price = scanner.nextDouble();
        scanner.nextLine();

        String query = "INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, name);
        stmt.setString(2, category);
        stmt.setInt(3, quantity);
        stmt.setDouble(4, price);
        stmt.executeUpdate();
        System.out.println("Product added successfully!");
    }

    public static void updateProduct() throws SQLException {
        System.out.print("Enter Product ID to update: ");
        int id = scanner.nextInt();
        scanner.nextLine();
        String q = "select id from products";
        Statement st1 = conn.createStatement();
        ResultSet rs = st1.executeQuery(q);
        boolean f = false;
        while (rs.next()) {
            int check;
            check = rs.getInt("id");
            if (check == id) {
                f = true;

            }
        }
        if (f == true) {
            System.out.print("Enter New Name: ");
            String name = scanner.nextLine();
            System.out.print("Enter New Quantity: ");
            int quantity = scanner.nextInt();
            System.out.print("Enter New Price: ");
            double price = scanner.nextDouble();
            scanner.nextLine();

            String query = "UPDATE products SET name=?, quantity=?, price=? WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, name);
            stmt.setInt(2, quantity);
            stmt.setDouble(3, price);
            stmt.setInt(4, id);
            stmt.executeUpdate();
            System.out.println("Product updated successfully!");
        } else {
            System.out.println("please enter the valid product id number");
        }
    }

    public static void deleteProduct() throws SQLException {

        System.out.print("Enter Product ID to delete: ");
        int id = scanner.nextInt();
        scanner.nextLine();
        String q = "select id from products";
        Statement st1 = conn.createStatement();
        ResultSet rs = st1.executeQuery(q);
        boolean f = false;
        while (rs.next()) {
            int check;
            check = rs.getInt("id");
            if (check == id) {
                f = true;

            }
        }
        if (f == true) {
            String query = "DELETE FROM products WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            stmt.executeUpdate();
            System.out.println("Product deleted successfully!");
        } else {
            System.out.println("please enter valid product id");
        }
    }

    public static void stockIn() throws SQLException {
        System.out.print("Enter Product ID: ");
        int id = scanner.nextInt();
        String q = "SELECT id FROM products";
        Statement st1 = conn.createStatement();
        ResultSet rs = st1.executeQuery(q);
        boolean f = false;
        while (rs.next()) {
            int check = rs.getInt("id");
            if (check == id) {
                f = true;
            }
        }
        if (f) {
            String qe = "SELECT quantity FROM products WHERE id = ?";
            PreparedStatement st = conn.prepareStatement(qe);
            st.setInt(1, id);
            ResultSet r = st.executeQuery();
            if (r.next()) {
                System.out.println("Selected product previous quantity is: " + r.getInt("quantity"));
            } else {
                System.out.println("No quantity found for this product.");
                return;
            }
            System.out.print("Enter Quantity to Add: ");
            int quantity = scanner.nextInt();
            scanner.nextLine();

            String query = "UPDATE products SET quantity = quantity + ? WHERE id = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, quantity);
            stmt.setInt(2, id);
            stmt.executeUpdate();
            System.out.println("Stock updated successfully!");
        } else {
            System.out.println("Please enter a valid product ID");
        }
    }

    public static void stockOut() throws SQLException {
        System.out.print("Enter Product ID: ");
        int id = scanner.nextInt();
        String q = "SELECT id FROM products";
        Statement st1 = conn.createStatement();
        ResultSet rs = st1.executeQuery(q);
        boolean f = false;
        while (rs.next()) {
            int check = rs.getInt("id");
            if (check == id) {
                f = true;
            }
        }
        if (f) {
            String qe = "SELECT quantity FROM products WHERE id = ?";
            PreparedStatement st = conn.prepareStatement(qe);
            st.setInt(1, id);
            ResultSet r = st.executeQuery();
            if (r.next()) {
                System.out.println("Selected product previous quantity is: " + r.getInt("quantity"));
            } else {
                System.out.println("No quantity found for this product.");
                return;
            }
            System.out.print("Enter Quantity to Reduce: ");
            int quantity = scanner.nextInt();
            scanner.nextLine();

            String query = "UPDATE products SET quantity = quantity - ? WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, quantity);
            stmt.setInt(2, id);
            stmt.executeUpdate();
            System.out.println("Stock reduced successfully!");
        }
    }

    public static void manageSuppliers() throws SQLException {
        while (true) {
            System.out.println("\n===== SUPPLIER MANAGEMENT =====");
            System.out.println("1. View Suppliers");
            System.out.println("2. Add Supplier");
            System.out.println("3. Delete Supplier");
            System.out.println("4. Back to Main Menu");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    viewSuppliers();
                    break;
                case 2:
                    addSupplier();
                    break;
                case 3:
                    deleteSupplier();
                    break;
                case 4: {
                    return;

                }
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }

    public static void viewSuppliers() throws SQLException {
        String query = "SELECT * FROM suppliers";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);

        System.out.println("\nID | Name | Contact | Address");
        System.out.println("-----------------------------------------");
        while (rs.next()) {
            System.out.println(rs.getInt("id") + " | " + rs.getString("name") + " | "
                    + rs.getString("contact") + " | " + rs.getString("address"));
        }
    }

    public static void addSupplier() throws SQLException {
        System.out.print("Enter Supplier Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Contact: ");
        String contact = scanner.nextLine();
        System.out.print("Enter Address: ");
        String address = scanner.nextLine();

        String query = "INSERT INTO suppliers (name, contact, address) VALUES (?, ?, ?)";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, name);
        stmt.setString(2, contact);
        stmt.setString(3, address);
        stmt.executeUpdate();
        System.out.println("Supplier added successfully!");
    }

    public static void deleteSupplier() throws SQLException {
        System.out.print("Enter Supplier ID to delete: ");
        int id = scanner.nextInt();

        scanner.nextLine();
        String q = "select id from suppliers";
        Statement st1 = conn.createStatement();
        ResultSet rs = st1.executeQuery(q);
        boolean f = false;
        while (rs.next()) {
            int check;
            check = rs.getInt("id");
            if (check == id) {
                f = true;

            }
        }
        if (f) {
            String query = "DELETE FROM suppliers WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, id);
            stmt.executeUpdate();
            System.out.println("Supplier deleted successfully!");
        } else {
            System.out.println("please enter valid supplier id");
        }
    }

    public static void manageCustomers() throws SQLException {
        while (true) {
            System.out.println("\n===== CUSTOMER MANAGEMENT =====");
            System.out.println("1. View Customers");
            System.out.println("2. Add Customer");
            System.out.println("3. Delete Customer");
            System.out.println("4. Back to Main Menu");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    viewCustomers();
                    break;
                case 2:
                    addCustomer();
                    break;
                case 3:
                    deleteCustomer();
                    break;
                case 4: {
                    return;
                }
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }

    public static void viewCustomers() throws SQLException {
        String query = "SELECT * FROM customers";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);

        System.out.println("\nID | Name | Contact | Address");
        System.out.println("-----------------------------------------");
        while (rs.next()) {
            System.out.println(rs.getInt("id") + " | " + rs.getString("name") + " | "
                    + rs.getString("contact") + " | " + rs.getString("address"));
        }
    }

    public static void addCustomer() throws SQLException {
        System.out.print("Enter Customer Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Contact: ");
        String contact = scanner.nextLine();
        System.out.print("Enter Address: ");
        String address = scanner.nextLine();

        String query = "INSERT INTO customers (name, contact, address) VALUES (?, ?, ?)";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1, name);
        stmt.setString(2, contact);
        stmt.setString(3, address);
        stmt.executeUpdate();
        System.out.println("Customer added successfully!");
    }

    public static void deleteCustomer() throws SQLException {
        System.out.print("Enter Customer ID to delete: ");
        int id = scanner.nextInt();
        scanner.nextLine();
        String checkQuery = "SELECT COUNT(*) FROM customers WHERE id = ?";
        try (PreparedStatement checkStmt = conn.prepareStatement(checkQuery)) {
            checkStmt.setInt(1, id);
            try (ResultSet rs = checkStmt.executeQuery()) {
                rs.next();
                int count = rs.getInt(1);
                if (count == 0) {
                    System.out.println("Please enter a valid customer ID");
                    return;
                }
            }
        } catch (SQLException e) {
            System.out.println("Error checking customer ID: " + e.getMessage());
            throw e;
        }
        String query = "DELETE FROM customers WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, id);
            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Customer deleted successfully!");
            } else {
                System.out.println("Failed to delete customer.");
            }
        } catch (SQLException e) {
            System.out.println("Error deleting customer: " + e.getMessage());
            throw e;
        }
    }

    public static void closeConnection() {
        try {
            if (conn != null) {
                conn.close();
                System.out.println("Database connection closed.");
            }
        } catch (SQLException e) {
            System.err.println("Error closing connection: " + e.getMessage());
}
}
}
