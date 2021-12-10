using UnityEngine;

public class PlayerPaddle : Paddle
{
    public Vector2 direction { get; private set; }
    public string pos;

    private void Update()
    {
        switch (this.pos)
        {
            case "up":
                this.movePaddleTop();
                break;
            case "middle":
                this.movePaddleMiddle();
                break;
            case "down":
                this.movePaddleBottom();
                break;
        }

        if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow))
        {
            //this.direction = Vector2.up
            if (this.pos == "down")
            {
                this.pos = "middle";
            }
            else if (this.pos == "middle")
            {
                this.pos = "up";
            }
            else
            {
                this.pos = "up";
            }
        }
        else if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow))
        {
            //this.direction = Vector2.down
            if (this.pos == "up")
            {
                this.pos = "middle";
            }
            else if (this.pos == "middle")
            {
                this.pos = "down";
            }
            else
            {
                this.pos = "down";
            }
        }
    }

    public void movePaddleTop()
    {
        Debug.Log("up");
        this.rigidbody.position = new Vector2(this.rigidbody.position.x, 3.4f);
        this.pos = "up";
    }

    public void movePaddleMiddle()
    {
        this.rigidbody.position = new Vector2(this.rigidbody.position.x, 0f);
        Debug.Log("middle");
        this.pos = "middle";

    }

    public void movePaddleBottom()
    {
        this.rigidbody.position = new Vector2(this.rigidbody.position.x, -3.4f);
        Debug.Log("down");
        this.pos = "down";
    }

    private void FixedUpdate()
    {
        if (this.direction.sqrMagnitude != 0)
        {
            this.rigidbody.AddForce(this.direction * this.speed);
        }
    }

}