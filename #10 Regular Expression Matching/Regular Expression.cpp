#include<iostream>
#include<string>

using namespace std;

bool isMatch(string s, string p) {

	if (p.length() == 0) return s.length() == 0;

	bool dot = p[0] == '.';
	bool wildcard = p[1] == '*';
	if (dot){
		if (wildcard){
			for (int i = 0; i <= s.length(); i++){
				if (isMatch(s.substr(i), p.substr(2))) return true;
			}
			return false;
		}
		else {
			if (s.length() == 0) return false;
			return isMatch(s.substr(1), p.substr(1));
		}
	}
	else {
		if (wildcard){
			for (int i = 0; i <= s.length(); i++){
				if (i == 0 || s[i - 1] == p[0]){
					if (isMatch(s.substr(i), p.substr(2))) return true;
				}
				else return false;
			}
			return false;
		}
		else {
			if (s.length() == 0) return false;
			return s[0] == p[0] && isMatch(s.substr(1), p.substr(1));
		}
	}
}

int main()
{
	string s = "ab";
	string p = ".*c";
	cout << isMatch(s, p);
}