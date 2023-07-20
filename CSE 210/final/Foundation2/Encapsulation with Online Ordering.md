The program is a simple order management system that loads customer information and order details from text files and performs various operations based on that data. It demonstrates the concept of encapsulation by defining classes and using them to encapsulate related data and behavior.

Here's an overview of how the modified program works:
1. The `Customer` class represents a customer and stores their ID, name, and address. It also provides methods for checking if the customer is in the USA and getting the shipping cost.

2. The `Address` class represents a customer's address and provides methods for determining if it is in the USA and generating a string representation of the address.

3. The `Product` class represents a product and stores its name, ID, price, and quantity. It provides methods to get the price, name, ID, and quantity of the product.

4. The `Order` class represents an order and contains a list of products and the corresponding customer. It provides methods to add products to the order, calculate the total price of the order (including shipping cost), and generate packing and shipping labels.

5. The `Program` class contains the `Main` method, which serves as the entry point of the program. It loads customer information and order details from text files using the `LoadCustomersFromFile` and `LoadOrdersFromFile` methods, respectively. It then iterates through the orders, printing packing labels, shipping labels, and total prices for each order.


Encapsulation in the program:
1. Data encapsulation: The classes (`Customer`, `Address`, `Product`, and `Order`) encapsulate data by defining private fields to store their respective information (`name`, `ID`, `price`, etc.). These fields are not directly accessible from outside the class but are accessed through public methods (`GetPrice()`, `GetName()`, etc.), which provide controlled access to the data. This encapsulation helps maintain data integrity and allows for easier maintenance and modification of the class's internal implementation.

2. Behavior encapsulation: The classes encapsulate behavior by providing methods (`GetTotalPrice()`, `AddProduct()`, `GetPackingLabel()`, etc.) that define the operations performed on the data. These methods encapsulate the logic for performing specific actions and hide the internal implementation details from the calling code. The calling code interacts with the classes through these methods, which ensures that the behavior is consistent and controlled.

3. Object composition: The `Order` class encapsulates a list of `Product` objects and a `Customer` object. This composition allows the `Order` class to manage and interact with the related objects as a cohesive unit. The `Order` class encapsulates the complexity of managing multiple products and their quantities for a specific customer, providing a higher-level abstraction to the calling code.

Encapsulation in the program helps organize and structure the data and behavior into meaningful units (classes), allowing for better code organization, data protection, and code reuse. It also promotes modularity and abstraction, making the code more maintainable and extensible.