import 'package:flutter/material.dart';
import 'screens/product_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tienda CRUD',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: ProductScreen(),
    );
  }
}
