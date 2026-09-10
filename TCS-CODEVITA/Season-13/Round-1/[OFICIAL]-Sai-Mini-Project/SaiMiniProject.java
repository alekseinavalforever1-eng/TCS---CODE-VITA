import java.util.*;

public class SaiMiniProject {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int initialBalance = sc.nextInt();
        int n = sc.nextInt();
        sc.nextLine();

        int balance = initialBalance;

        List<String> transactions = new ArrayList<>();
        List<Integer> transactionValues = new ArrayList<>();
        List<Integer> commits = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().split(" ");

            switch (parts[0]) {
                case "read":
                    System.out.println(balance);
                    break;

                case "credit":
                    int creditAmount = Integer.parseInt(parts[1]);
                    balance += creditAmount;
                    transactions.add("credit");
                    transactionValues.add(creditAmount);
                    break;

                case "debit":
                    int debitAmount = Integer.parseInt(parts[1]);
                    balance -= debitAmount;
                    transactions.add("debit");
                    transactionValues.add(debitAmount);
                    break;

                case "abort":
                    int txnIndex = Integer.parseInt(parts[1]) - 1;
                    if (txnIndex < transactions.size()) {
                        String txnType = transactions.get(txnIndex);
                        int value = transactionValues.get(txnIndex);
                        if (txnType.equals("credit")) balance -= value;
                        else if (txnType.equals("debit")) balance += value;
                        transactions.set(txnIndex, "aborted");
                    }
                    break;

                case "rollback":
                    int commitIndex = Integer.parseInt(parts[1]) - 1;
                    if (commitIndex < commits.size()) {
                        balance = commits.get(commitIndex);
                        transactions.clear();
                        transactionValues.clear();
                    }
                    break;

                case "commit":
                    commits.add(balance);
                    transactions.clear();
                    transactionValues.clear();
                    break;
            }
        }
        sc.close();
    }
}
