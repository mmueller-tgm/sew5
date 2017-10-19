package primeSearcher;

import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicLong;

public class primeSearcher extends Thread {
	AtomicLong lastPrime = new AtomicLong();
	AtomicBoolean running = new AtomicBoolean(true);
	
	@Override
	public void run() {
		// loop through the numbers one by one
		for (long n = new Long("1000000000000001"); running.get(); n++) {
			boolean prime = true;
			
			for (long j = 2; j<n ; j++) {
				if (n%j == 0) {
					prime = false;
					break; // exit the inner for loop
				}
			}
			if (prime && n != 1) {
				lastPrime.set(n);
				System.out.println(lastPrime.get());
			}
		}
		System.out.println("primeSearcherTM stopped");
	}
	
	public void terminate() {
		running.set(false);
	}
	
	public Long getPrime(){
		return lastPrime.get();
	}

}
