#include <cstdio>
#include <vector>

using namespace std;

const int maxn = 1e5 + 10;

vector<int> G[maxn];
int A[maxn];
int dp[maxn][3];
long long ans;

void dfs(int u, int fa)
{
	for (int v : G[u])
	{
		if (v == fa)
			continue;
		dfs(v, u);
		if (A[u] >= A[v])
		{
			ans += 1ll * dp[u][0] * dp[v][1];
			ans += 1ll * dp[u][0] * dp[v][2];
			ans += 1ll * dp[u][1] * dp[v][2];
		}
		if (A[u] <= A[v])
		{
			ans += 1ll * dp[u][1] * dp[v][0];
			ans += 1ll * dp[u][2] * dp[v][0];
			ans += 1ll * dp[u][2] * dp[v][1];
		}
		ans += 1ll * dp[u][1] * dp[v][1];
		if (A[u] > A[v])
			dp[u][2] += dp[v][2] + dp[v][1];
		else if (A[u] < A[v])
			dp[u][0] += dp[v][0] + dp[v][1];
		else
		{
			dp[u][0] += dp[v][0];
			dp[u][1] += dp[v][1];
			dp[u][2] += dp[v][2];
		}
	}
	ans += dp[u][0] + dp[u][1] + dp[u][2];
	++dp[u][1];
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
		scanf("%d", &A[i]);
	for (int i = 1; i < n; ++i)
	{
		int u, v;
		scanf("%d %d", &u, &v);
		G[u].push_back(v);
		G[v].push_back(u);
	}
	dfs(1, 0);
	printf("%lld\n", ans);
	return 0;
}
