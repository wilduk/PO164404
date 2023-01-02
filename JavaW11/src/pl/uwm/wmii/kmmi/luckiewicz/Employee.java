package pl.uwm.wmii.kmmi.luckiewicz;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

class Employee
{

	public Employee(String name, double salary, LocalDate hireDay)
	{
		this.name = name;
		this.salary = salary;

		LocalDate calendar = LocalDate.of(hireDay.getYear(), hireDay.getMonth(), hireDay.getDayOfMonth());
		hireDay_ = Date.from(calendar.atStartOfDay(ZoneId.systemDefault()).toInstant());

		// Dodane w stosunku do poprzedniej wersji
		id = nextId;
		++nextId;
	}

	public Employee(String name, double salary, int year, int month, int day)
	{
		new Employee(name, salary, LocalDate.of(year, month, day));
	}

	public String getName()
	{
		return name;
	}

	public double getSalary()
	{
		return salary;
	}

	public Date getHireDay()
	{
		return (Date) hireDay_.clone();
	}

	public void raiseSalary(double procent)
	{
		double raise = salary * procent / 100;
		salary += raise;
	}

	// Dodane w stosunku do poprzedniej wersji
	public int getId()
	{
		return id;
	}

	// Dodane w stosunku do poprzedniej wersji
	public void setId()
	{
		id = nextId;
		++nextId;
	}

	// Dodane w stosunku do poprzedniej wersji
	public static int getNextId()
	{
		return nextId;
	}

	private String name;
	private double salary;
	private Date hireDay_;

	// Dodane w stosunku do poprzedniej wersji
	private int id;
	private static int nextId = 1;
}