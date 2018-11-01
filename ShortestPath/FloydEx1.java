// Floyd Algorithm

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
//測試用路徑{{1,2,2},{1,3,6},{1,4,4},{2,3,3},{3,1,7},{3,4,1},{4,1,5},{4,3,12}}
//4 8
//1 2 2
//1 3 6
//1 4 4
//2 3 3
//3 1 7
//3 4 1
//4 1 5
//4 3 12

public class FloydEx1 {

	int input_n() { // 輸入點數
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		System.out.print("Total numbers of points:");
		int n = sc.nextInt();
		return n;
	}

	int[] input_SE() { // 輸入點數
		int[] n = new int[2];
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		System.out.print("Strat from:");
		n[0] = sc.nextInt();
		System.out.print("End in:");
		n[1] = sc.nextInt();
		return n;
	}

	int[][] input_e(int n) { // 輸入路徑，n為點數
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int[][] e = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i != j) {
					System.out.printf(
							"The distance from point %d to point %d"
									+ "(Please insert 999, if %d doesn't connect with %d):",
							i + 1, j + 1, i + 1, j + 1);
					e[i][j] = sc.nextInt(); // 未排除輸入字串問題
				} else
					e[i][j] = 0;
			}
		}
		return e;
	}

	int[][][] floyd(int[][] e, int n) { // 替換過程
		int[][] path = new int[n][n];
		System.out.println();
		// n=1; //測試用
		// int k=0; //測試用
		for (int k = 0; k < n; k++) { // 必經k
			for (int i = 0; i < n; i++) { // 到(i,j)點
				for (int j = 0; j < n; j++) {
					if (e[i][j] > e[i][k] + e[k][j]) { // 如果
						e[i][j] = e[i][k] + e[k][j];
						path[i][j] = k + 1;
					}
				}
			}
		}
		int[][][] E = new int[2][n][n];
		E[0] = e;
		E[1] = path; // E[0]為最短
		return E;
	}

	void print_e(int[][] e) { // 印出結果矩陣
		for (int i = 0; i < e.length; i++) {
			for (int j = 0; j < e[i].length; j++) {
				System.out.print(e[i][j] + " ");
			}
			System.out.println();
		}
	}

	void get_path(int Start, int End, int[][] path, int[][] result) { // S為起點，E為終點
		List<Integer> p = new ArrayList<Integer>(); // 用於存取最短路徑
		p.add(End);
		int S = Start - 1;
		int E = End - 1;
		while (path[S][E] != 0) {
			p.add(0, path[S][E]);
			E = path[S][E] - 1;
		}
		p.add(0, Start);
		System.out.println("result:");
		System.out.printf("\tThe path from %d to %d is: ", Start, End);
		for (int i = 0; i < p.size(); i++) {
			System.out.print(p.get(i) + " ");
		}
		System.out.printf("\n\tThe distance from %d to %d is %d", Start, End, result[Start - 1][End - 1]);
	}

	public static void main(String[] args) {
		// int[][] E;
		int[][] E = { { 0, 2, 6, 4 }, { 999, 0, 3, 999 }, { 7, 999, 0, 1 }, { 5, 999, 12, 0 } }; // 測試用路徑
		int[][][] F;
		int[] SE;
		// int[] SE = {4,3}; //測試用:起點終點
		// int N;
		int N = 4; // 測試用

		FloydEx1 P = new FloydEx1();

		// N=P.input_n(); //輸入點數
		// E=P.input_e(N); //輸入路徑
		SE = P.input_SE();// 輸入起點&終點

		F = P.floyd(E, N); // 計算

		// P.print_e(F[0]); // 測試用:印出結果表
		// P.print_e(F[1]); //測試用:印出路徑表
		P.get_path(SE[0], SE[1], F[1], F[0]); // 取得路徑

	}

}
