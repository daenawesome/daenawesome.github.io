using System;
using System.Collections.Generic;
using System.IO;

// This modified program to show creativity and exceed requirements now loads customer and order data from text files

public class Program
{
    public static void Main(string[] args)
    {
        // File paths for customer and order data
        string customerFilePath = "customer.txt";
        string orderFilePath = "order.txt";

        // Check if both customer and order files exist
        if (!File.Exists(customerFilePath) || !File.Exists(orderFilePath))
        {
            Console.WriteLine("One or both of the files customer.txt and order.txt are missing.");
            return;
        }

        // Load customers from the customer file
        List<Customer> customers = LoadCustomersFromFile(customerFilePath);

        // Check if there are any customers loaded
        if (customers.Count == 0)
        {
            Console.WriteLine("customer.txt file is empty.");
            return;
        }

        // Load orders from the order file and associate them with customers
        List<Order> orders = LoadOrdersFromFile(orderFilePath, customers);

        // Check if there are any orders loaded
        if (orders.Count == 0)
        {
            Console.WriteLine("order.txt file is empty.");
            return;
        }

        // Process each order and display information
        for (int i = 0; i < orders.Count; i++)
        {
            Order order = orders[i];
            int orderNumber = i + 1;

            Console.WriteLine("-------------------------------------------------------------------------");
            Console.WriteLine($"Order {orderNumber} Packing Label:");
            Console.WriteLine(order.GetPackingLabel());
            Console.WriteLine();

            Console.WriteLine($"Order {orderNumber} Shipping Label:");
            Console.WriteLine(order.GetShippingLabel());
            Console.WriteLine();

            Console.WriteLine($"Order {orderNumber} Total Price: ${order.GetTotalPrice()}");
            Console.WriteLine("-------------------------------------------------------------------------");
        }
    }

    // Load customer data from a file and create a list of customers
    public static List<Customer> LoadCustomersFromFile(string filePath)
    {
        List<Customer> customers = new List<Customer>();
        string[] lines = File.ReadAllLines(filePath);

        Customer customer = null;

        foreach (string line in lines)
        {
            if (line.StartsWith("Customer_Id:"))
            {
                // Create a new customer and add it to the list
                if (customer != null)
                {
                    customers.Add(customer);
                }

                // Parse the customer ID from the line
                int customerId = int.Parse(line.Split(':')[1].Trim());
                customer = new Customer(customerId);
            }
            else if (line.StartsWith("Customer_Name:"))
            {
                // Set the customer name
                string customerName = line.Split(':')[1].Trim();
                customer.Name = customerName;
            }
            else if (line.StartsWith("Customer_Address:"))
            {
                // Parse the customer address and set it
                string customerAddress = line.Split(':')[1].Trim();
                customer.Address = ParseAddress(customerAddress);
            }
        }

        // Add the last customer to the list if it exists
        if (customer != null)
        {
            customers.Add(customer);
        }

        return customers;
    }

    // Load order data from a file, associate orders with customers, and create a list of orders
    public static List<Order> LoadOrdersFromFile(string filePath, List<Customer> customers)
    {
        List<Order> orders = new List<Order>();
        string[] lines = File.ReadAllLines(filePath);

        Order order = null;
        int lineNumber = 0;

        while (lineNumber < lines.Length)
        {
            string line = lines[lineNumber];
            lineNumber++;

            if (line.StartsWith("Customer_Id:"))
            {
                // Parse the customer ID from the line and find the associated customer
                int customerId = int.Parse(line.Split(':')[1].Trim());
                Customer customer = customers.Find(c => c.Id == customerId);

                // Create a new order associated with the customer
                order = new Order(customer);
            }
            else if (line.StartsWith("Product_Id:"))
            {
                // Parse product details from subsequent lines and create a product object
                string productId = line.Split(':')[1].Trim();

                string productName = GetValue(lines[lineNumber]);
                lineNumber++;
                string productPrice = GetValue(lines[lineNumber]);
                lineNumber++;
                string productQuantity = GetValue(lines[lineNumber]);
                lineNumber++;

                Product product = new Product(productName, productId, double.Parse(productPrice), int.Parse(productQuantity));

                // Add the product to the current order
                order.AddProduct(product);
            }
            else if (line.StartsWith("-- End of Order List for"))
            {
                // Add the completed order to the list
                orders.Add(order);
            }
        }

        return orders;
    }

    // Helper method to extract the value from a line of the format "Key: Value"
    private static string GetValue(string line)
    {
        return line.Split(':')[1].Trim();
    }

    // Parse an address string into an Address object
    public static Address ParseAddress(string addressString)
    {
        string[] addressParts = addressString.Split(',');
        string streetAddress = addressParts[0].Trim();
        string city = addressParts[1].Trim();
        string stateProvince = addressParts[2].Trim();
        string country = addressParts[3].Trim();

        return new Address(streetAddress, city, stateProvince, country);
    }
}

public class Order
{
    private List<Product> products;
    private Customer customer;

    public Order(Customer customer)
    {
        // Initialize the product list and associate the customer
        this.products = new List<Product>();
        this.customer = customer;
    }

    // Add a product to the order
    public void AddProduct(Product product)
    {
        products.Add(product);
    }

    // Calculate the total price of the order, including product prices and shipping cost
    public double GetTotalPrice()
    {
        double totalPrice = 0;

        foreach (Product product in products)
        {
            totalPrice += product.GetPrice();
        }

        totalPrice += customer.GetShippingCost();

        return totalPrice;
    }

    // Generate a packing label for the order
    public string GetPackingLabel()
    {
        string packingLabel = "Packing Label:\n";

        foreach (Product product in products)
        {
            packingLabel += $">> Name/Id/Quantity: {product.GetName()}, Product ID: {product.GetProductId()}, {product.GetQuantity()}\n";
        }

        return packingLabel;
    }

    // Generate a shipping label for the order, including customer name and address
    public string GetShippingLabel()
    {
        string shippingLabel = "Shipping Label:\n";
        shippingLabel += $">> Customer Name: {customer.Name}\n";
        shippingLabel += customer.Address.ToString();

        return shippingLabel;
    }
}

public class Product
{
    private string name;
    private string productId;
    private double price;
    private int quantity;

    public Product(string name, string productId, double price, int quantity)
    {
        this.name = name;
        this.productId = productId;
        this.price = price;
        this.quantity = quantity;
    }

    // Calculate the total price of the product(s) in the order
    public double GetPrice()
    {
        return price * quantity;
    }

    // Get the product name
    public string GetName()
    {
        return name;
    }

    // Get the product ID
    public string GetProductId()
    {
        return productId;
    }

    // Get the quantity of the product
    public int GetQuantity()
    {
        return quantity;
    }
}

public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }
    public Address Address { get; set; }

    public Customer(int id)
    {
        Id = id;
    }

    // Check if the customer's address is in the USA
    public bool IsInUSA()
    {
        return Address.IsInUSA();
    }

    // Get the shipping cost for the customer's address
    public double GetShippingCost()
    {
        return IsInUSA() ? 5 : 35;
    }
}

public class Address
{
    private string streetAddress;
    private string city;
    private string stateProvince;
    private string country;

    public Address(string streetAddress, string city, string stateProvince, string country)
    {
        this.streetAddress = streetAddress;
        this.city = city;
        this.stateProvince = stateProvince;
        this.country = country;
    }

    // Check if the address is in the USA
    public bool IsInUSA()
    {
        return string.Equals(country, "USA", StringComparison.OrdinalIgnoreCase);
    }

    // Override the ToString method to display the address details
    public override string ToString()
    {
        return $">> Street Address: {streetAddress}\n>> City: {city}\n>> State/Province: {stateProvince}\n>> Country: {country}";
    }
}
