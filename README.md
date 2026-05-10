# DSA-Practice 🚀

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Data+Structures+%26+Algorithms;LeetCode+%7C+GeeksforGeeks+Practice;Consistency+is+the+Key+🔥;Cracking+Coding+Interviews+🚀" />
</p>

---

## 👨‍💻 About This Repository

This repository contains my daily **Data Structures & Algorithms** practice for improving problem-solving skills and preparing for coding interviews at product-based and service-based companies.

I regularly solve problems from:

- LeetCode
- GeeksforGeeks
- Coding Platforms

with optimized approaches, clean code, and complexity analysis.

---

# 🎯 Goals

- Solve 2–3 problems daily
- Master core DSA concepts
- Improve coding interview skills
- Build consistency in problem solving
- Prepare for internships & placements

---

# 🛠 Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=cpp,java,python,git,github,vscode" />
</p>

---

# 📂 Repository Structure

```bash
DSA-Practice/
│
├── LeetCode/
│   ├── Arrays/
│   ├── Strings/
│   ├── Trees/
│   ├── Graphs/
│   ├── DP/
│   └── ...
│
├── GeeksforGeeks/
│
├── Notes/
│
├── progress.md
│
└── README.md
```

---

# 📚 Topics Covered

- Arrays
- Strings
- Linked Lists
- Stacks & Queues
- Trees
- Graphs
- Binary Search
- Sliding Window
- Greedy Algorithms
- Dynamic Programming
- Backtracking
- Recursion

---

# 📈 LeetCode Stats

<p align="center">
  <img src="https://leetcard.jacoblin.cool/YOUR_LEETCODE_USERNAME?theme=dark&font=Nunito&ext=heatmap" />
</p>

---

# 🔥 GitHub Stats

<p align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=YOUR_GITHUB_USERNAME&show_icons=true&theme=tokyonight" />
  
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_GITHUB_USERNAME&layout=compact&theme=tokyonight" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=YOUR_GITHUB_USERNAME&theme=tokyonight" />
</p>

---

# 🚀 Daily Progress Tracker

I maintain a `progress.md` file to track:

- Problems solved
- Approaches used
- Time & Space complexities
- Learnings & mistakes

---

# ✨ Example Solution Format

```cpp
// Problem: Two Sum
// Platform: LeetCode
// Topic: Arrays + HashMap
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int,int> mp;

        for(int i=0;i<nums.size();i++) {

            int rem = target - nums[i];

            if(mp.count(rem))
                return {mp[rem], i};

            mp[nums[i]] = i;
        }

        return {};
    }
};
```

---

# 🏆 Coding Profiles

<p align="left">

<a href="https://leetcode.com/u/YOUR_LEETCODE_USERNAME/">
  <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/>
</a>

<a href="https://www.geeksforgeeks.org/user/YOUR_GFG_USERNAME/">
  <img src="https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white"/>
</a>

<a href="https://github.com/YOUR_GITHUB_USERNAME">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

</p>

---

# 🌟 Future Plans

- Solve 500+ DSA problems
- Participate in coding contests
- Add company-wise interview questions
- Upload optimized solutions
- Improve contest rating

---

# 💡 Quote

> “Consistency beats motivation.”

---

# ⭐ Support

If you like this repository, give it a ⭐ and follow my coding journey 🚀
