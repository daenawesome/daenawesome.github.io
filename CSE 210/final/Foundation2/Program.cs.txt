using System;
using System.Collections.Generic;

// The program creates customers, products, and orders, and then displays the packing labels, shipping labels, and total prices for each order.

public class Program
{
    public static void Main(string[] args)
    {
        // Create customers
        Address customerAddress1 = new Address("123 Main St", "New York", "NY", "USA");
        Customer customer1 = new Customer("John Smith", customerAddress1);

        Address customerAddress2 = new Address("456 Elm St", "London", "", "UK");
        Customer customer2 = new Customer("Jane Doe", customerAddress2);

        // Create products
        Product product1 = new Product("Product A", "A001", 10.99, 2);
        Product product2 = new Product("Product B", "B002", 5.49, 3);
        Product product3 = new Product("Product C", "C003", 8.99, 1);

        // Create orders
        Order order1 = new Order(customer1);
        order1.AddProduct(product1);
        order1.AddProduct(product2);

        Order order2 = new Order(customer2);
        order2.AddProduct(product2);
        order2.AddProduct(product3);

        // Display packing labels, shipping labels, and total prices
        Console.WriteLine("Order 1 Packing Label:\n" + order1.GetPackingLabel());
        Console.WriteLine("Order 1 Shipping Label:\n" + order1.GetShippingLabel());
        Console.WriteLine("Order 1 Total Price: $" + order1.GetTotalPrice());

        Console.WriteLine();

        Console.WriteLine("Order 2 Packing Label:\n" + order2.GetPackingLabel());
        Console.WriteLine("Order 2 Shipping Label:\n" + order2.GetShippingLabel());
        Console.WriteLine("Order 2 Total Price: $" + order2.GetTotalPrice());
    }
}

public class Order
{
    private List<Product> products; // List of products in the order
    private Customer customer; // Customer who placed the order

    public Order(Customer customer)
    {
        this.products = new List<Product>();
        this.customer = customer;
    }

    public void AddProduct(Product product)
    {
        products.Add(product); // Add a product to the order
    }

    public double GetTotalPrice()
    {
        double totalPrice = 0;

        foreach (Product product in products)
        {
            totalPrice += product.GetPrice(); // Calculate the total price of all products in the order
        }

        totalPrice += customer.GetShippingCost(); // Add shipping cost based on the customer's location

        return totalPrice; // Return the total price including shipping cost
    }

    public string GetPackingLabel()
    {
        string packingLabel = "Packing Label:\n";

        foreach (Product product in products)
        {
            packingLabel += $"Name: {product.GetName()}, Product ID: {product.GetProductId()}\n";
        }

        return packingLabel; // Return the packing label for the order
    }

    public string GetShippingLabel()
    {
        return "Shipping Label:\n" + customer.GetAddress().ToString(); // Return the shipping label with the customer's address
    }
}

public class Product
{
    private string name; // Product name
    private string productId; // Product ID
    private double price; // Price per unit
    private int quantity; // Quantity ordered

    public Product(string name, string productId, double price, int quantity)
    {
        this.name = name;
        this.productId = productId;
        this.price = price;
        this.quantity = quantity;
    }

    public double GetPrice()
    {
        return price * quantity; // Calculate the total price of the product based on the quantity
    }

    public string GetName()
    {
        return name; // Return the product name
    }

    public string GetProductId()
    {
        return productId; // Return the product ID
    }
}

public class Customer
{
    private string name; // Customer name
    private Address address; // Customer address

    public Customer(string name, Address address)
    {
        this.name = name;
        this.address = address;
    }

    public bool IsInUSA()
    {
        return address.IsInUSA(); // Check if the customer's address is in the USA
    }

    public double GetShippingCost()
    {
        return IsInUSA() ? 5 : 35; // Return the shipping cost based on the customer's location
    }

    public Address GetAddress()
    {
        return address; // Return the customer's address
    }
}

public class Address
{
    private string streetAddress; // Street address
    private string city; // City
    private string stateProvince; // State or province
    private string country; // Country

    public Address(string streetAddress, string city, string stateProvince, string country)
    {
        this.streetAddress = streetAddress;
        this.city = city;
        this.stateProvince = stateProvince;
        this.country = country;
    }

    public bool IsInUSA()
    {
        return string.Equals(country, "USA", StringComparison.OrdinalIgnoreCase); // Check if the address is in the USA
    }

    public override string ToString()
    {
        return $"Street Address: {streetAddress}\nCity: {city}\nState/Province: {stateProvince}\nCountry: {country}"; // Return a formatted string representation of the address
    }
}
