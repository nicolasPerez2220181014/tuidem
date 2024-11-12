import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = 'http://127.0.0.1:8000/api';

  Future<List<dynamic>> fetchItems(String endpoint) async {
    final response = await http.get(Uri.parse('$baseUrl/$endpoint/'));
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load items');
    }
  }

  Future<void> createItem(String endpoint, Map<String, dynamic> data) async {
    final response = await http.post(
      Uri.parse('$baseUrl/$endpoint/'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(data),
    );
    if (response.statusCode != 201) {
      throw Exception('Failed to create item');
    }
  }

  Future<void> updateItem(String endpoint, int id, Map<String, dynamic> data) async {
    final response = await http.put(
      Uri.parse('$baseUrl/$endpoint/$id/'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(data),
    );
    if (response.statusCode != 200) {
      throw Exception('Failed to update item');
    }
  }

  Future<void> deleteItem(String endpoint, int id) async {
    final response = await http.delete(Uri.parse('$baseUrl/$endpoint/$id/'));
    if (response.statusCode != 204) {
      throw Exception('Failed to delete item');
    }
  }
}
