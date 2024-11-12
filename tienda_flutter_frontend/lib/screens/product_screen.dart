import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ProductScreen extends StatefulWidget {
  @override
  _ProductScreenState createState() => _ProductScreenState();
}

class _ProductScreenState extends State<ProductScreen> {
  final ApiService apiService = ApiService();
  List<dynamic> products = [];

  @override
  void initState() {
    super.initState();
    fetchProducts();
  }

  void fetchProducts() async {
    products = await apiService.fetchItems('products');
    setState(() {});
  }

  void createProduct() async {
    await apiService.createItem('products', {'name': 'New Product', 'price': 10.0, 'stock': 5});
    fetchProducts();
  }

  void updateProduct(int id) async {
    await apiService.updateItem('products', id, {'name': 'Updated Product', 'price': 15.0, 'stock': 10});
    fetchProducts();
  }

  void deleteProduct(int id) async {
    await apiService.deleteItem('products', id);
    fetchProducts();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Products')),
      body: ListView.builder(
        itemCount: products.length,
        itemBuilder: (context, index) {
          final product = products[index];
          return ListTile(
            title: Text(product['name']),
            subtitle: Text('Price: ${product['price']} - Stock: ${product['stock']}'),
            trailing: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(icon: Icon(Icons.edit), onPressed: () => updateProduct(product['id'])),
                IconButton(icon: Icon(Icons.delete), onPressed: () => deleteProduct(product['id'])),
              ],
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: createProduct,
        child: Icon(Icons.add),
      ),
    );
  }
}
