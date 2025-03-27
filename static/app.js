const API_URL = "/api/employees";

async function loadEmployees() {
  const res = await fetch(API_URL);
  const data = await res.json();
  const list = document.getElementById("employeeList");
  list.innerHTML = "";

  data.forEach(emp => {
    const li = document.createElement("li");
    li.innerHTML = `
      ${emp.name} - ${emp.position}
      <button onclick="deleteEmployee('${emp.id}')">Delete</button>
      <button onclick="updateEmployee('${emp.id}')">Update</button>
    `;
    list.appendChild(li);
  });
}

async function addEmployee() {
  const name = document.getElementById("name").value;
  const position = document.getElementById("position").value;

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, position }),
  });
  loadEmployees();
}

async function deleteEmployee(id) {
  await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  loadEmployees();
}

async function updateEmployee(id) {
  const name = prompt("Enter new name:");
  const position = prompt("Enter new position:");

  await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, position }),
  });
  loadEmployees();
}

loadEmployees();
