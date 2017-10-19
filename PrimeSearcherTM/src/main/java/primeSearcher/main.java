package primeSearcher;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import primeSearcher.primeSearcher;
import java.util.Date;

public class main extends HttpServlet{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	Boolean first = true;
	primeSearcher ps = new primeSearcher();
	Date start = new Date();
	
	
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
			throws ServletException, IOException {
		if (first) {
			ps.start();
			System.out.println("Computing started");
		}
		first = false; 
		PrintWriter out = resp.getWriter();
		long prime = ps.getPrime();
		String prime_str;
		if (prime == 0){
			prime_str = "No prime above 1000000000000001 yet found!";
		} else {
			prime_str = ""+prime;
		}
		String s = "<html><head><title>" + prime_str + 
				"</title></head><body><h1>" + prime_str + 
				"</h1><br><h1>Server running since " + start.toLocaleString() + 
				"</h1></body></html>";
		out.print(s);
	}
	
	@Override
	public void destroy() {
		ps.terminate();
		super.destroy();
	}
}
