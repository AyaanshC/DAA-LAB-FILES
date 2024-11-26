#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

int root_value = 0;

// Node class
class Node {
public:
    char ch;
    int freq;
    Node* left;
    Node* right;

    Node(char character, int frequency) {
        ch = character;
        freq = frequency;
        left = right = NULL;
    }
};

// Comparator class
class Compare {
public:
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Calculating frequency of each character (Hashmap)
unordered_map<char, int> calculateFrequency(const string& str) {
    unordered_map<char, int> freqMap;
    for (char ch : str) {
        freqMap[ch]++;
    }
    return freqMap;
}

// Constructing Huffman Tree
Node* buildHuffmanTree(unordered_map<char, int>& freqMap, int root_value) {
    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (auto pair : freqMap) {
        pq.push(new Node(pair.first, pair.second));
    }

    while (pq.size() > 1) {
        Node* left = pq.top(); 
        pq.pop();
        Node* right = pq.top(); 
        pq.pop();
        Node* newNode = new Node('\0', left->freq + right->freq);  
        root_value += newNode->freq;
        newNode->left = left;
        newNode->right = right;
        pq.push(newNode);
    }

    return pq.top();
}

// Alloting code to each character 
void assignCodes(Node* root, string code, unordered_map<char, string>& huffmanCodes) {
    if (!root) return;
    if (root->ch != '\0') {
        huffmanCodes[root->ch] = code;
    }
    assignCodes(root->left, code + "0", huffmanCodes);
    assignCodes(root->right, code + "1", huffmanCodes);
}

// Compressing the input string (into binary codes)
string compressString(const string& str, unordered_map<char, string>& huffmanCodes) {
    string compressed = "";
    for (char ch : str) {
        compressed += huffmanCodes[ch];
    }
    return compressed;
}

// Calculating compression ratio
void calculateCompressionRatio(const string& original, const string& compressed) {
    int originalSize = original.size() * 8;
    int compressedSize = compressed.size();
    cout<<"Orginal size: "<<originalSize/8<<" bytes"<<endl;
    cout<<"Compressed size: "<<compressedSize/8<<" bytes"<<endl;
    cout<<"Compression Ratio: "<<(double)originalSize/compressedSize<<endl;
}

// Read text file
string readTextFile(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: File '" << filename << "' does not exist or cannot be opened." << endl;
        return "";
    }
    
    stringstream buffer;
    buffer << file.rdbuf();
    string content = buffer.str();

    // Check if file is empty or contains only whitespace
    if (content.empty() || all_of(content.begin(), content.end(), ::isspace)) {
        cerr << "Error: File '" << filename << "' contains no readable text or characters." << endl;
        return "";
    }

    return content;
}

int main() {
    string filename;
    cout << "Enter the filename of the text file: ";
    cin >> filename;

    string input = readTextFile(filename);
    if (input.empty()) {
        cerr << "No data to process." << endl;
        return 1;
    }

    unordered_map<char, int> freqMap = calculateFrequency(input);
    Node* root = buildHuffmanTree(freqMap, root_value);

    unordered_map<char, string> huffmanCodes;
    assignCodes(root, "", huffmanCodes);

    string compressedString = compressString(input, huffmanCodes);
    calculateCompressionRatio(input, compressedString);

    return 0;
}